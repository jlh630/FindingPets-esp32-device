from net.wifi import *
from mqtt_client import MQTTClient
from lcd.lcd_1602 import *
from gps.uart_nen6m import GpsMoule
from gps.location import Location
import json
from Message import Message

device_id = 10

subscribe_topic = b"status/"+str(device_id)
publish_topic = "device/"+str(device_id)

lock = True


# 连接wifi模块
if not wifi_connect('k70','wk66666666'):
    raise Exception("wifi 连接失败") 

#mqttclient的回调函数
def sub_cb(topic, msg): 
    msg=msg.decode('utf-8').strip()
    print(topic, msg)
    try:
        message=Message.from_dict(json.loads(msg))
        global lock
        if message.code == 0 :
            lock = True
        else:
            lock = False
    except:
        pass

# 建立一个MQTT客户端
socket = MQTTClient("esp32_mqtt_client", "mqtt.jianglh.icu",8883,"device","device123",60,True)
# 设置回调函数
socket.set_callback(sub_cb)
# 建立连接
socket.connect()

print("mqtt_server connect successly")

# socket.publish('status/'+str(device_id),'ok',retain=True,qos=1)

# 订阅
socket.subscribe(subscribe_topic)  

#初始化gps
gpsmoule = GpsMoule()

#lcd_1602
lcd=uselcd()

while True:
    socket.check_msg()
    if not lock:
        if gpsmoule.uart.any():
            location = gpsmoule.readline()
            if location is not None :
                print(location)
                lcd.clear()
                lcd.putstr("lat:{}  {}\n".format(round(location.latitude, 4),location.time.split(':')[0]))
                lcd.putstr("lon:{} {}{}".format(round(location.longitude, 4),location.time.split(':')[1],count))
                socket.publish(publish_topic,str(json.dumps(location).__dict__),retain=False,qos=0)
            else :
                lcd.clear()
                lcd.putstr("Searching gps ...")
    else:
        lcd.clear()
        lcd.putstr("DeviceId:{}\n unactivated !!!".format(device_id))
    time.sleep(1)
    
wifi_disconnect()
