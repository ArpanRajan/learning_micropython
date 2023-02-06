from machine import Pin

import utime

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
while(True):
    if button.value() == 1:
        led.toggle()
        utime.sleep(.200) # try to wait for the human to react, reaction time is 150-300ms