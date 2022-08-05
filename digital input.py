from machine import Pin
from time import sleep

input_pin = Pin(15, Pin.IN, Pin.PULL_UP)#
led = Pin(25, Pin.OUT)

while(True):
    input_state = input_pin.value()#read the value of the import pin
    if(input_state ==True):
        led.value(1)
    else:
        led.value(0)
    sleep(1)