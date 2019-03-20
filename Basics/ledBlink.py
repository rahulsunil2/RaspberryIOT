import RPi.GPIO as led
import time
led.setmode(led.BOARD)
led_pins = [3, 5, 7, 11, 13, 15, 19, 21]
led.setwarnings(False)
for i in led_pins:
    led.setup(i, led.OUT)
while True:
    for i in led_pins:
        led.output(i, 1)
        time.sleep(0.05)
        led.output(i, 0)
        time.sleep(0.05)
    
    
    
    
    
    
    
    
