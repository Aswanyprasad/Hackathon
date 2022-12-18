from datetime import date, datetime
import schedule
import time

name = input("enter the name:")
print (name)
message = input("enter your message")
def msg():
    print(message)

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

d = date(year, month, day)
print(d)

    # 👇️ date and time
hours = int(input('Enter the hour: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))
t = date(hours,minutes,seconds)

current_time = (d,t)

dt = datetime(year, month, day, hours, minutes, seconds)

print(dt)

if ( date==d , time == t ):
    msg()




