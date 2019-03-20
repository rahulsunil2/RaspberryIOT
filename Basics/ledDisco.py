import RPi.GPIO as led
import time
led.setmode(led.BOARD)
led_pins_1 = [3, 5, 7, 11,13,15,19,21]
led_pins_2 = [13, 15, 19, 21]
led.setwarnings(False)
for i in range(4):
    led.setup(led_pins_1[i], led.OUT)
    led.setup(led_pins_2[i], led.OUT)
while True:
    for i in range(8):
        if(i%2==0):
            led.output(led_pins_1[i], 1)
            time.sleep(1)
    for i in range(7,-1,-1):
        if(i%2==0):
            led.output(led_pins_1[i], 0)
            time.sleep(1)
    
    
    
    