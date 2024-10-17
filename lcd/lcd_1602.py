from machine import SoftI2C, Pin
from lcd.i2c_lcd import I2cLcd
import time

def uselcd():
    DEFAULT_I2C_ADDR = 0x27
    i2c = SoftI2C(sda=Pin(15),scl=Pin(2),freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear()
    return lcd
