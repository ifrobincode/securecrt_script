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
                 'display fan',
                 'display transceiver diagnosis interface',
                 'display environment',
                 'display power',
                 'display boot-loader',
                 'display cpu',
                 'display cpu history',
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

# 弹出窗口，提示工程师输入支持的设备类型
input_type = xsh.Dialog.Prompt('请输入支持的设备类型：\n  cisco、huawei、h3c、asa、nxos、'
                               '\n  a10、ruijie、linux', '请确认设备类型', '', 0)

# 设置屏幕同步
xsh.Screen.Synchronous = True


# 遍历设备类型的巡检命令列表，发送命令
def send_cmds(cmds_list):
    xsh.Screen.Send('\n' * 3)
    for cmd in cmds_list:
        xsh.Screen.Send(cmd + '\n' * 4)
        xsh.Session.Sleep(100)


# 如果输入的设备类型在支持列表中，调用发送命令函数，否则弹出窗口提示设备类型错误
if input_type in supported_devices_type:
    send_cmds(cmds_dict[input_type])  # 发送命令，根据输入的设备类型，传入不同的命令
else:
    xsh.Dialog.MessageBox('尚不支持的设备类型！', '设备类型错误', 48)

