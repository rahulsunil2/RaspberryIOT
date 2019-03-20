__author__ = 'arun'


import time
# import numpy as np
# import thread
import httplib, urllib,ftplib




while(1):

    p1=35
    p2="hello world"

    print p1
    params = urllib.urlencode({'field1': p1, 'key':'F9R9LTSMWF5Z40BU'})
    # params = urllib.urlencode({'field2': p1, 'key':'T4NUNVKIB7Z149I5'})
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    #conn.request("POST", "/update", params, headers)
    conn.request("POST", "/update", params)
    response = conn.getresponse()

    print response.status, response.reason

    data = response.read()
    conn.close()

    time.sleep(16)
    params = urllib.urlencode({'field2': p2, 'key':'F9R9LTSMWF5Z40BU'})
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    #conn.request("POST", "/update", params, headers)
    conn.request("POST", "/update", params)
    response = conn.getresponse()

    print response.status, response.reason

    data = response.read()
    conn.close()

    time.sleep(16)

ser.close()




