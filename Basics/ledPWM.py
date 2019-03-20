import RPi.GPIO as led
import time
led.setmode(led.BOARD)
led_pin = 5

led.setwarnings(False)
led.setup(led_pin,led.OUT)
pwm_led = led.PWM(led_pin, 1000)
pwm_led.start(0)

while True:
    for x in range(100):
        print(x)
        pwm_led.ChangeDutyCycle(x)
        time.sleep(0.1)
    for x in range(100,-1,-1):
        print(x)
        pwm_led.ChangeDutyCycle(x)
        time.sleep(0.1)
        
    