import RPi.GPIO as sw
import time
sw.setmode(sw.BOARD)
sw.setwarnings(False)

sw_pin=23
led_pin=29
sw.setup(sw_pin,sw.IN,pull_up_down=sw.PUD_UP)

sw.setup(led_pin,sw.OUT)
sw.output(led_pin,1)
x=1
while(1):
    x=sw.input(sw_pin)
    if(x==0):
        sw.output(led_pin,1)
    else:
        sw.output(led_pin,0)
