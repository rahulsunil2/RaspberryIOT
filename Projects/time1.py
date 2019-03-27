import time
import datetime
i = datetime.datetime.now()
print("dd/mm/yyyy format = %s/%s/%s" % (i.day,i.month,i.year))

print("Current hour = %s" %i.hour)

print("Current minute = %s" %i.minute)

print("Current second = %s" %i.second)

print("hh:hh:ss format = %s:%s:%s" % (i.hour,i.minute,i.second))

h = int(input("Enter the hour : "))
m = int(input("Enter the minute : "))

while True:
    i=datetime.datetime.now()
    print("hh:hh:ss format = %s:%s:%s" % (i.hour,i.minute,i.second))
    time.sleep(1)
    if h==int(i.hour) and m==int(i.minute):
        print("Alert")
        
        



      
