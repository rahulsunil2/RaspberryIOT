from time import sleep
from datetime import datetime
from pygame import mixer

currentTime = datetime.now()

mixer.init()
alert = mixer.Sound('bell.wav')


print("Date : %s/%s/%s" % (currentTime.day, currentTime.month, currentTime.year))
print("Time : %s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))

timeList = []

alarmLimit = int(input("Enter the No: of Alarms to be set : "))

for i in range(alarmLimit):
	print("\n")
	print("Enter the time for Alarm %d" % (i+1))
	h = int(input("Enter the Hour : "))
	m = int(input("Enter the Minute : "))
	t = int(input("Ring the bell for how long : "))
	timeList.append([h, m, t])

timeList.sort()

timerCount = 0

while timerCount < alarmLimit:
	currentTime = datetime.now()
	print("Current Time : %s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))
	if (int(currentTime.hour) == timeList[timerCount][0]) and (int(currentTime.minute) == timeList[timerCount][1]):
		for count in range(timeList[timerCount][2]):
			print(count)
			alert.play()
			sleep(1)
		bufferCurrentTime = datetime.now()
		print("Current Time : %s:%s:%s" % (bufferCurrentTime.hour, bufferCurrentTime.minute, bufferCurrentTime.second))
		remainingTime = 60 - timeList[timerCount][2]
		sleep(remainingTime)
		timerCount += 1
		continue
	sleep(1)

