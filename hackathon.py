from datetime import date, datetime


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

d = date(year, month, day)
print(d)

# ---------------------------------------

# 👇️ date and time

hours = int(input('Enter the hour: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))


dt = datetime(year, month, day, hours, minutes, seconds)

print (dt)
from selenium import webdriver

driver = webdriver.chrome()
driver.get('https://web.whatsapp.com/')

name = input("enter the name of usr or group:")
msg = input("enter your message:")
count = int(input("enter the count:"))
input("enter anything after scanning QR code")
user=driver.find_element_by_xpath('//span[@title="{}]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('input-container')
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_class_name('compose-btn-send')
    button.click()
