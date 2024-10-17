# FindingPets-esp32-device
是FindingPetsSys的esp32单片机上的代码。
## 设备:
1.esp32 \
2.lcd1602 \ 
3.neo-6m gps模块 \
## 基本原理
使用esp32中自带wifi模块连接上网络后，使用mqtts协议连接mqtt服务端，neo-6m收集当前的gps位置信息，数据上报到mqtt服务端。