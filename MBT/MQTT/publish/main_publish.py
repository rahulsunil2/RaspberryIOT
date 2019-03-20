# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("iot.eclipse.org", 1883)
mqttc.publish("testTopic/testing", "Welcome to Open Source")
mqttc.loop(2) #timeout = 2s
