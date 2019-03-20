import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
red = 3
GPIO.setup(red,GPIO.OUT)
GPIO.output(red,GPIO.HIGH)
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("IEDC")

def on_message(client, userdata, msg):
	print str(msg.payload)
	if 'redon' in str(msg.payload):
	    GPIO.output(red,GPIO.LOW)
	elif 'redoff' in str(msg.payload):
	    GPIO.output(red,GPIO.HIGH)
		
client = mqtt.Client()
print("Running")
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
