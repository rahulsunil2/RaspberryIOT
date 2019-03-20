# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

while 1:
    mqttc = mqtt.Client("python_pub")
    mqttc.connect("iot.eclipse.org", 1883)
    mqttc.publish("testing/123", "Welcome to Open Source")
    mqttc.loop(2) #timeout = 2s
    time.sleep(2)
