from machine import Pin

p13 = Pin(13, Pin.OUT)    # create output pin on GPIO0                # set pin to "on" (high) level
p13.off()                # set pin to "off" (low) level

def on():
    p13.on()

def off():
    p13.off()
