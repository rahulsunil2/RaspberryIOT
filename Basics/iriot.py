import RPi.GPIO as sw
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("iot.eclipse.org", 1883)


sw.setmode(sw.BOARD)
sw.setwarnings(False)

sw_pin=23
sw.setup(sw_pin,sw.IN,pull_up_down=sw.PUD_UP)

n=0

while True:
    x=sw.input(sw_pin)
    if(x==0):
        mqttc.publish("IR", "Detected")
	n+=1
	print(n)
#    else:
#	mqttc.publish("IR", "Not Detected")

