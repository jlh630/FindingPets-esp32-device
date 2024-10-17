from machine import Pin

p15 = Pin(15, Pin.OUT)    # create output pin on GPIO0                # set pin to "on" (high) level
p15.off()                # set pin to "off" (low) level

def on():
    p15.on()

def off():
    p15.off()

