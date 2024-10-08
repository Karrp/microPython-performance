# boot.py -- run on boot-up
    ## Original boot file on ESP32 S3 ##
    # This file is executed on every boot (including wake-boot from deepsleep)
    #import esp
    #esp.osdebug(None)
    #import webrepl
    #webrepl.start()

from machine import Pin, reset
from sys import modules

led = Pin(21, Pin.OUT)
    # led.value(0) - LED on
    # led.value(1) - LED off

btn = Pin(0, Pin.IN, Pin.PULL_UP)
    # btn.value() == 0 - button pressed

def reload(mod): # reload module
    mod_name = mod.__name__
    del modules[mod_name]
    return __import__(mod_name)

# Not working on boot or in main.py
# def del_len():
#     try:
#         del(len)
#         print("len deleted")
#     except:
#         print("len not exists")

# del_len()

exec(open("del_len.py").read())