from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random

string.alphanum='1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.


# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "727080"

# The Write API Key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "CHXZRKPTROQBBTKE"

# The Hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any Username.
mqttUsername = "TSMQTTRpiDemo"

# Your MQTT API Key from Account > My Profile.
mqttAPIKey ="JLM5KBZ55SJ3RAPY"

# Set the transport mode to WebSockets.
tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

while(1):

    clientID = ''

# Create a random clientID.
    for x in range(1,16):
        clientID+=random.choice(string.alphanum)

    # get the system performance data over 20 seconds.
    cpuPercent = psutil.cpu_percent(interval=20)
    ramPercent = psutil.virtual_memory().percent

    # build the payload string.
    payload = "field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)


    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
	print (" Published CPU =",cpuPercent," RAM =", ramPercent," to host: " , mqttHost , " clientID= " , clientID)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")