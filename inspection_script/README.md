# 简介

- 工作中经常需要对客户的网络设备进行巡检，如果工程师PC可以接入到客户的网络中去使用远程登录的方式巡检（如SSH），使用[Devices_Inspection脚本](https://github.com/icefire-ken/Devices_Inspection)
就可以完成巡检操作；

- 但是偶尔也会遇到直接从Console口登录设备进行巡检的情况，就需要从SecureCRT（或Xshell）软件依次输入多个命令收集巡检信息的操作；

- 本脚本可以在SecureCRT中运行，利用脚本代替手动输入巡检命令的过程。

# 使用方法

1. 在SecureCRT的Session Options —— Terminal —— Mapped Keys， 映射快捷键（如F1），Function选择Run Script，选择本脚本。

   在Xshell的工具 —— 按键对应 —— 新建，提示输入快捷键（如F1），操作类型选择运行脚本，在路径上选择本脚本。

2. 之后，按F1执行脚本会弹出如下提示：

   ![device_types.png](https://github.com/icefire-ken/securecrt_script/blob/master/images/device_types.png)

   按提示输入正确的【设备类型】就可以开始巡检了。

# 使用方法v3

- v3脚本使用本地的Python 3.x环境，不需要安装SecureCRT内置的Python 2.7环境。

- v3脚本涉及从info.xlsx文件中读取巡检命令，本地Python 3.x需要安装第三方模块pandas与openpyxl。

- info.xlsx文件模板请从另一个仓库获取。[Devices_Inspection脚本](https://github.com/icefire-ken/Devices_Inspection)。

- 修改v3脚本内指定的info.xlsx文件路径，INFO_PATH。

## 注意事项：

- 本脚本只是代替人工手动输入巡检命令的过程，并不涉及登录。

- 巡检时记得开启记录Log Session记录回显内容。

- 执行脚本前CLI预先进入设备特权模式（用户视图），保证巡检命令能够被正确执行。

- 若运行脚本出现如下提示：

  ![crt95.png](https://github.com/icefire-ken/securecrt_script/blob/master/images/crt95.png)

  原因：

  从SecureCRT 9.5版本开始，安装时默认不再安装Python 2.7环境，需要手动勾选。

  解决方法：

  1、安装时勾选Python 2.7环境。

  2、安装后，在控制面板 —— 添加/删除程序，编辑安装好的SecureCRT，勾选添加Python 2.7环境。

  3、在PC上直接安装Python 3.x环境。（SecureCRT 9.5目前最高支持Python 3.11）

# 目前支持的设备类型

- cisco
- huawei
- h3c
- asa
- nxos
- a10
- ruijie
- linux

# 更新日志

详见 [UPDATE.md](https://github.com/ifrobincode/securecrt_script/blob/master/UPDATE.md)。


