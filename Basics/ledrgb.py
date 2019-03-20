import RPi.GPIO as led
import time

led.setwarnings(False)

led.setmode(led.BOARD)

led_pins = [11, 13, 15]

for x in led_pins:
    led.setup(x, led.OUT)
    
for x in led_pins:
    led.output(x, 1)

while (1):
    for x in led_pins:
        led.output(x, 0)
        time.sleep(0.1)
        led.output(x, 1)
        time.sleep(0.1)
        