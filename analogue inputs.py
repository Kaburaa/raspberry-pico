from machine import ADC

sensor_pin = ADC(26)

while(True):
    analog_value = sensor_pin.read_u16()
    print(analog_value)