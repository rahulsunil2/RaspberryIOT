import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


TRIG = 16
ECHO = 18

print ("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.OUT)

while True:
    GPIO.output(TRIG,False)
    print("Waiting for sensor to settle")
    time.sleep(2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        print("OFF")
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        print("ON")
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    distance = round(distance,2)
    
    if distance > 2 and distance < 400:
        print("Distance: ",distance -0.5)
    else:
        print("out of range")
