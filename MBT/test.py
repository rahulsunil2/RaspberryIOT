__author__ = 'ARUN'
# a = 10
# b = 20
# if a>b:
#     print 'a>b'
# else:
#     print 'b>a'a
import requests
import json
r = requests.get('https://api.thingspeak.com/channels/727055/feeds.json?api_key=N572DM3RA2J977MZ&results=2')
prrrr= json.loads(r.text)
# print prrrr['channel']
print prrrr
print prrrr['feeds'][0]['field2']