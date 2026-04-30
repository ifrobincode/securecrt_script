# 简介

- 在项目开局时，可能会需要对多台设备进行统一配置的情况。这些设备拥有许多相同配置，比如用户信息、NTP、SNMP等配置。也有一些不同的配置，比如 IP 地址、主机名等配置。
- 本脚本可以在项目开局阶段，用 Console 登录设备进行初始化配置的时候，简化初始化配置准备工作和配置过程。


# 脚本结构

- config_template.txt：配置模板文件。
- devices_vars.xlsx：设备变量文件。
- devices_config.py：脚本文件。

# 使用方法

1. 将所有需要配置的内容保存在 config_template.txt 文件中。
2. 将每台设备配置不相同的部分用变量形式填写，比如：${hostname}。相同配置保留即可。
3. 每台设备不相同的配置内容保存在 devices_vars.xlsx 文件中。每一行是一台设备的配置内容。每一列是相同变量的配置内容。
   - 如果有多个接口需要配置 IP 地址，则需要为变量添加前缀或后缀加以区分，比如：${g0/1_ip}、${g0/2_ip}。
4. 比如 hostname 列，它就是替换 config_template.txt 文件中的 ${hostname} 变量。根据不同设备，填写不同的内容。
5. 注意：devices_vars.xlsx 文件中的前两列，DEVICE_NAME 和 DEVICE_TYPE 列，是必须的。
6. DEVICE_NAME 是预定义的设备名称，在脚本执行时，会根据用户输入的 DEVICE_NAME 匹配将要配置的变量内容。
   - DEVICE_NAME只是预定义设备名称，并不是配置进设备的 Hostname，所以也可以用序号来代替。
7. DEVICE_TYPE 是预定义的设备类型，在脚本执行时，会根据用户输入的 DEVICE_NAME 选择进入/退出配置模式的命令。
8. 执行脚本时，会先提示用户输入 DEVICE_NAME，以此来确定用户要为哪一台设备进行配置，脚本会自动选择相关变量内容填入配置模板。
9. 然后会展示一个具体配置内容，提示用户是否继续。

## 注意事项：


# 目前支持的设备类型

- cisco
- h3c


# 更新日志

详见 [UPDATE.md](https://github.com/ifrobincode/securecrt_script/blob/master/config_script/UPDATE.md)。


