from machine import Pin
import time

led = Pin(28, Pin.OUT)
ldr = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if ldr.value():
       led.value(1)
       time.sleep(0.5)
        
    else:
        led.value(0)
        time.sleep(0.5)