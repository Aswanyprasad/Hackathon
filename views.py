import time
import datetime

# Get the current time
now = datetime.datetime.now()

# Calculate the scheduled time by adding one hour to the current time
scheduled_time = now + datetime.timedelta(hours=1)

# Convert the scheduled time to a timestamp
scheduled_timestamp = time.mktime(scheduled_time.timetuple())

# Pause the program until the scheduled time has arrived
while time.time() < scheduled_timestamp:
    time.sleep(1)

# Send the message
print("Sending message...")


