# $language = "Python"
# $interface = "1.0"

import pandas

INFO_PATH = r'D:\4_Learn\Python\devices_inspection\info.xlsx'

# 支持的设备类型
supported_devices_type = ['cisco', 'nxos', 'asa', 'huawei', 'h3c', 'a10', 'ruijie', 'linux']


def get_cmds_info(info_file):  # 获取info文件中的巡检命令
    try:  # 读取Excel文件第二张工作表的数据生成DataFrame
        cmds_dataframe = pandas.read_excel(info_file, sheet_name=1, dtype=str)
    except FileNotFoundError:  # 如果没有配置info文件或info文件名错误
        crt.Dialog.MessageBox(f"info文件不存在！", "文件错误", 48)
        return  # return none
    except ValueError:  # 捕获异常信息
        crt.Dialog.MessageBox(f"info文件缺失子表格信息！", "文件错误", 48)
        return  # return none
    else:
        cmds_dict = cmds_dataframe.to_dict('list')  # 将DataFrame转换成字典
        # "list"参数规定外层为字典，列标题为key，列下所有行内容以list形式为value的字典
        # 若有多列，代表字典内有多个key:value对
        return cmds_dict


def insert_cmds(cmds_dict, input_type):
    prepend_cmd = None
    append_cmd = None
    match input_type:
        case 'cisco_ios':
            prepend_cmd = 'terminal length 0'
            append_cmd = 'terminal length 24'
        case 'cisco_nxos':
            prepend_cmd = 'terminal length 0'
            append_cmd = 'terminal length 24'
        case 'cisco_asa':
            prepend_cmd = 'terminal pager 0'
            append_cmd = 'terminal pager 24'
        case 'huawei':
            prepend_cmd = 'screen-length 0 temporary'
            append_cmd = 'screen-length 24 temporary'
        case 'hp_comware':
            prepend_cmd = 'screen-length disable'
            append_cmd = 'undo screen-length disable'
        case 'a10':
            prepend_cmd = 'terminal length 0'
            append_cmd = 'terminal length 24'
        case 'ruijie_os':
            prepend_cmd = 'terminal length 0'
            append_cmd = 'terminal length 24'
    list = cmds_dict[input_type]
    list.insert(0, prepend_cmd)
    list.append(append_cmd)
    return list


# 遍历设备类型的巡检命令列表，发送命令
def send_cmds(cmds_list):
    crt.Screen.Send('\n' * 3)
    for cmd in cmds_list:
        if type(cmd) is str:
            crt.Screen.Send(cmd + '\n' * 4)
            crt.Sleep(100)


def main():
    # 获取info文件中的巡检命令
    cmds_dict = get_cmds_info(INFO_PATH)
    if not cmds_dict:  # 如果没有获取到命令列表
        crt.Dialog.MessageBox('获取命令列表失败！', '命令列表错误', 48)
        return

    # 弹出窗口，提示工程师输入支持的设备类型
    input_type = crt.Dialog.Prompt('请输入支持的设备类型：\n  cisco、nxos、asa、huawei、h3c、'
                                   '\n  a10、ruijie、linux', '请确认设备类型')

    # 检查用户是否输入了设备类型
    if not input_type:  # 如果没有输入任何设备类型
        crt.Dialog.MessageBox('未输入设备类型！', '输入错误', 48)

    elif input_type not in supported_devices_type:  # 如果输入的设备类型不在支持列表中
        crt.Dialog.MessageBox('尚不支持的设备类型！', '设备类型错误', 48)

    elif input_type in supported_devices_type:  # 如果输入的设备类型在支持列表中
        # 设置屏幕同步
        crt.Screen.Synchronous = True

        # 修改设备类型与info文件中设备类型对应关系
        match input_type:
            case 'cisco':
                input_type = 'cisco_ios'
            case 'nxos':
                input_type = 'cisco_nxos'
            case 'asa':
                input_type = 'cisco_asa'
            case 'huawei':
                input_type = 'huawei'
            case 'h3c':
                input_type = 'hp_comware'
            case 'a10':
                input_type = 'a10'
            case 'ruijie':
                input_type = 'ruijie_os'
            case 'linux':
                input_type = 'linux'

        # 获取对应设备的命令列表
        cmds_list = insert_cmds(cmds_dict, input_type)

        # 根据设备类型确定日志命令
        log_cmd = None
        match input_type:
            case 'cisco_ios':
                log_cmd = 'show logging'
            case 'cisco_nxos':
                log_cmd = 'show logging'
            case 'cisco_asa':
                log_cmd = 'show logging'
            case 'huawei':
                log_cmd = 'display log'
            case 'hp_comware':
                log_cmd = 'display log'
            case 'a10':
                log_cmd = 'show log'
            case 'ruijie_os':
                log_cmd = 'show logging'

        # 如果设备有日志命令，询问用户是否跳过
        if log_cmd and log_cmd in cmds_list:
            skip_log = crt.Dialog.MessageBox(
                f"是否跳过查看日志 '{log_cmd}'？\n查看日志可能会延长巡检过程。",  # 使用 str.format() 替换 f-string
                "跳过查看日志",
                4  # 4 表示对话框包含“是”和“否”按钮
            )
            if skip_log == 6:  # 用户点击了“是”
                cmds_list.remove(log_cmd)  # 从命令列表中移除日志命令

            # 发送命令
            send_cmds(cmds_list)


main()
