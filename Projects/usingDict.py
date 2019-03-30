from time import sleep
from datetime import datetime
from pygame import mixer

currentTime = datetime.now()

print("Date : %s/%s/%s" % (currentTime.day, currentTime.month, currentTime.year))
print("Time : %s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))

timeDict = {}

alarmLimit = int(input("Enter the No: of Alarms to be set : "))

for i in range(alarmLimit):
	print("Enter the time for Alarm %d" % (i))
	h = int(input("Enter the Hour : "))
	if h not in timeDict:
		timeDict[h] = []
	m = int(input("Enter the Minute : "))
	timeDict[h].append(m)

while True:
	currentTime = datetime.datetime.now()
    print("Time : %s:%s:%s" % (i.hour, i.minute, i.second))
    time.sleep(1)
    if (int(i.hour) in timeDict):