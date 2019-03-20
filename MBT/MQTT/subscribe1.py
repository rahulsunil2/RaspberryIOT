import paho.mqtt.client as mqtt

#while 1:
def on_connect(self,client, userdata, rc):
    print("Connected with result code "+str(rc))
    self.subscribe("testing/123")

def on_message(client, userdata, msg):
    print str(msg.payload)
    if 'redon' in str(msg.payload):
        print "Hello"
    elif 'redoff' in str(msg.payload):
        print "OK"

client = mqtt.Client("MQTT1")
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org",1883,60)
client.loop_forever()
