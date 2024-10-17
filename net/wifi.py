import network
import time
from machine import Pin

max_count = 5

p2 = Pin(2, Pin.OUT)
p2.off()
wlan = network.WLAN(network.STA_IF)

def wifi_connect(ssid , password):
    current = 0
    wlan.active(True)
    
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected() and current < max_count:
            current +=1
            time.sleep(1)
            print('...')
            
        if not wlan.isconnected():
            print('time_out')
            return False
        
    print('network config:', wlan.ifconfig())
    p2.on()
    return True

def wifi_disconnect():
    p2.off()
    wlan.disconnect()
    wlan.active(False)
