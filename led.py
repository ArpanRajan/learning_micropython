from machine import Pin

import utime

p = Pin(14, Pin.OUT)

while(True):
    p.toggle()
    utime.sleep(1)