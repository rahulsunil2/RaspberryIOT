import RPi.GPIO as led
import time
led.setmode(led.BOARD)
led.setwarnings(False)

# {"a" : 7, "b" : 11, "c" : 19, "d" : 15, "e" : 13, "f" : 5, "g" : 3}

led_pins   = [3, 5, 7, 11, 13, 15, 19, 21]


led_pins_0 = [5, 7, 11, 13, 15, 19]
led_pins_1 = [11, 19]
led_pins_2 = [7, 11, 3, 15, 13]
led_pins_3 = [7, 11, 19, 15, 3]
led_pins_4 = [5, 3, 11, 19]
led_pins_5 = [7, 5, 3, 19, 15]
led_pins_6 = [7, 5, 3, 19, 15, 13]
led_pins_7 = [7, 11, 19]
led_pins_8 = [3, 5, 7, 11, 13, 15, 19]
led_pins_9 = [3, 5, 7, 11, 15, 19]

digits = [led_pins_0,
led_pins_1,
led_pins_2,
led_pins_3,
led_pins_4,
led_pins_5,
led_pins_6,
led_pins_7,
led_pins_8,
led_pins_9]

for x in led_pins:
    led.setup(x, led.OUT)
    led.output(x, 0)
    
while True:
    for i in digits:
        for j in i:
            led.output(j, 1)
        time.sleep(1)
        for j in i:
             led.output(j, 0)