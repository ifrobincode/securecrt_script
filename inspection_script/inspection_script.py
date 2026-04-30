# $language = "Python"
# $interface = "1.0"

# 设备类型巡检命令列表
cisco_cmds_list = ['terminal length 0',
                   'show clock detail',
                   'show inventory',
                   'show env all',
                   'show module all',
                   'show environment',
                   'show power',
                   'show redundancy',
                   'show redundancy switchover history',
                   'dir',
                   'show boot',
                   'show processes cpu',
                   'show processes memory',
                   'show license udi',
                   'show license all',
                   'show license feature',
                   'show logging',
                   'show version',
                   'show vtp status',
                   'show vtp password',
                   'show vlan brief',
                   'show ip interface brief',
                   'show interfaces status',
                   'show cdp neighbors',
                   'show ip route',
                   'show ip ospf neighbor',
                   'show ip ospf interface brief',
                   'show ip eigrp neighbors',
                   'show ip eigrp interfaces',
                   'verify /md5 system:running-config',
                   'show running-config',
                   'terminal length 24']

huawei_cmds_list = ['screen-length 0 temporary',
                    'display clock',
                    'display device esn',
                    'display elabel brief',
                    'display environment',
                    'display power',
                    'dir flash:',
                    'display cpu',
                    'display cpu history',
                    'display memory',
                    'display license',
                    'display log',
                    'display version',
                    'display vlan',
                    'display interface brief',
                    'display ip interface brief',
                    'display lldp neighbor brief',
                    'display ip routing-table',
                    'display ospf peer',
                    'display ospf interface',
                    'display current-configuration',
                    'screen-length 24 temporary']

h3c_cmds_list = ['screen-length disable',
                 'display clock',
                 'display device manuinfo',
                 'dir',
                 'display fan',
                 'display transceiver diagnosis interface',
                 'display environment',
                 'display power',
                 'display boot-loader',
                 'display cpu',
                 'display memory summary',
                 'display license',
                 'display license feature',
                 'display log',
                 'display version',
                 'display vlan brief',
                 'display interface brief',
                 'display ip interface brief',
                 'display lldp neighbor-information list',
                 'display ip routing-table',
                 'display ospf peer',
                 'display ospf interface',
                 'display vrrp',
                 'display current-configuration',
                 'undo screen-length disable']

ciscoasa_cmds_list = ['terminal pager 0',
                      'show inventory',
                      'dir',
                      'show bootvar',
                      'show cpu usage detailed',
                      'show memory',
                      'show license udi',
                      'show license all',
                      'show license feature',
                      'show logging',
                      'show version',
                      'show failover state',
                      'show failover',
                      'show vlan',
                      'show interface ip brief',
                      'show interfaces status',
                      'show route',
                      'show ospf neighbor',
                      'show ospf interface brief',
                      'show eigrp neighbors',
                      'show eigrp interfaces',
                      'verify /md5 system:running-config',
                      'show running-config',
                      'terminal pager 24']

nxos_cmds_list = ['terminal length 0',
                  'show clock detail',
                  'show inventory',
                  'show module',
                  'show environment',
                  'show vdc',
                  'show redundancy status',
                  'show vpc',
                  'dir',
                  'show boot',
                  'show processes cpu',
                  'show processes memory',
                  'show license',
                  'show license host-id',
                  'show license usage',
                  'show logging',
                  'show version',
                  'show vtp status',
                  'show vtp password',
                  'show vlan brief',
                  'show fex',
                  'show ip interface brief',
                  'show interface brief',
                  'show interfaces status',
                  'show cdp neighbors',
                  'show ip route',
                  'show ip ospf neighbor',
                  'show ip ospf interface brief',
                  'show ip eigrp neighbors',
                  'show ip eigrp interfaces',
                  'show running-config',
                  'terminal length 24']

a10_cmds_list = ['terminal length 0',
                 'show clock',
                 'show version',
                 'show environment',
                 'show cpu',
                 'show memory',
                 'show disk',
                 'show log',
                 'show ip interfaces',
                 'show interfaces brief',
                 'show vrrp-a',
                 'show ip route',
                 'show gslb group brief',
                 'show running-config',
                 'terminal length 24']

ruijie_cmds_list = ['terminal length 0',
                    'show clock',
                    'show cpu',
                    'show memory',
                    'show license all-license',
                    'show logging',
                    'show version',
                    'show vlan',
                    'show ip interface brief',
                    'show interfaces status',
                    'show lldp neighbors',
                    'show ip route',
                    'show ip ospf neighbor',
                    'show ip ospf interface brief',
                    'show running-config',
                    'terminal length 24']

linux_cmds_list = ['uname -a',
                   'head -n 1 /etc/issue',
                   'cat /proc/cpuinfo',
                   'hostname',
                   'ipconfig',
                   'iptables -L',
                   'route -n',
                   'netstat -lntp']

fortinet_cmds_list = []

juniper_junos_cmds_list = []

# 巡检命令集合字典
cmds_dict = {'cisco': cisco_cmds_list,
             'huawei': huawei_cmds_list,
             'h3c': h3c_cmds_list,
             'asa': ciscoasa_cmds_list,
             'nxos': nxos_cmds_list,
             'a10': a10_cmds_list,
             'ruijie': ruijie_cmds_list,
             'linux': linux_cmds_list,
             }

# 支持的设备类型
supported_devices_type = ['cisco', 'huawei', 'h3c', 'asa', 'nxos', 'a10', 'ruijie', 'linux']


def get_cmds_info(info_file):  # 获取info文件中的巡检命令
    try:  # 读取Excel文件第二张工作表的数据生成DataFrame
        cmds_dataframe = pandas.read_excel(info_file, sheet_name=2, dtype=str)
    except FileNotFoundError:  # 如果没有配置info文件或info文件名错误
        crt.Dialog.MessageBox(f"info文件不存在！", "文件错误", 48)
        sys.exit(1)  # 异常退出
    except ValueError:  # 捕获异常信息
        crt.Dialog.MessageBox(f"info文件缺失子表格信息！", "文件错误", 48)
        sys.exit(1)  # 异常退出
    else:
        cmds_dict = cmds_dataframe.to_dict('list')  # 将DataFrame转换成字典
        # "list"参数规定外层为字典，列标题为key，列下所有行内容以list形式为value的字典
        # 若有多列，代表字典内有多个key:value对
        return cmds_dict


# 遍历设备类型的巡检命令列表，发送命令
def send_cmds(cmds_list):
    crt.Screen.Send('\n' * 3)
    for cmd in cmds_list:
        crt.Screen.Send(cmd + '\n' * 4)
        crt.Sleep(100)


def main():
    # 弹出窗口，提示工程师输入支持的设备类型
    input_type = crt.Dialog.Prompt('请输入支持的设备类型：\n  cisco、huawei、h3c、asa、nxos、'
                                   '\n  a10、ruijie、linux', '请确认设备类型')

    # 检查用户是否输入了设备类型
    if not input_type:  # 如果没有输入任何设备类型
        crt.Dialog.MessageBox('未输入设备类型！', '输入错误', 48)

    elif input_type not in supported_devices_type:  # 如果输入的设备类型不在支持列表中
        crt.Dialog.MessageBox('尚不支持的设备类型！', '设备类型错误', 48)

    elif input_type in supported_devices_type:  # 如果输入的设备类型在支持列表中
        # 设置屏幕同步
        crt.Screen.Synchronous = True

        # 获取对应设备的命令列表
        cmds_list = cmds_dict[input_type]

        # 根据设备类型确定日志命令
        log_cmd = None
        match input_type:
            case 'cisco':
                log_cmd = 'show logging'
            case 'huawei':
                log_cmd = 'display log'
            case 'h3c':
                log_cmd = 'display log'
            case 'asa':
                log_cmd = 'show logging'
            case 'nxos':
                log_cmd = 'show logging'
            case 'a10':
                log_cmd = 'show log'
            case 'ruijie':
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
