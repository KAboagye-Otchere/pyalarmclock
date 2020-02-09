#Author Kwabena Aboagye-Otchere
#Simple Alarm clock implementation which tells the current time and allows you to set an alarm

import time
import datetime
import winsound

def alarm():
    print("Enter the time you want to wake up in H:M format")
    time.sleep(1)
    print ("Eg. 17:45")
    alarm_time = input(">> ")
    alarm_time = alarm_time.split(":")
    alarm_time = list(map(int, alarm_time))

    #Conversions for hours and minutes to seconds
    hms = [3600, 60]
    alarm_seconds = sum([a*b for a,b in zip(hms[:len(alarm_time)], alarm_time)])

    # Get the current time of day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(hms, [now.hour, now.minute, now.second])])

    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds

    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
            time_diff_seconds += 86400 # number of seconds in a day

    # Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)

    # Alarm beeping
    winsound.Beep(3000,100)
    winsound.Beep(2500,100)
    winsound.Beep(2000,100)    
    winsound.Beep(1000,100)    
    winsound.Beep(500,100)
    print("Wake Up!")
    
    
    

def clock():
    print("Hello..")
    time.sleep(2)
    print ("1 -> Get current time")
    print ("2 -> Set alarm")
    operation = int(input("Enter number of corresponding operation you want to do: "))
    try:
        if operation == 1:
            print(time.ctime(time.time()))

        elif operation == 2:
            alarm()
        else:
            print ("Incorrect input")
            time.sleep(2)
            clock()
            
            
    #Exception thrown to catch errors from user input
    except ValueError:
        print ("Incorrect input")
        time.sleep(2)
        clock()

clock()
    
