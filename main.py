import time
from plyer import notification
# In this project we will make a water reminder program

user = int(input("Enter Minutes To Remind: "))
result = user*60

while True:
    print("Time to drink water!!")
    notification.notify(title="Water Reminder", message = "it's time to drink water")
    time.sleep(result)