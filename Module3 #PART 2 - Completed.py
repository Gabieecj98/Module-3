Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #PART 2
>>> 
>>> Current_Time = int(input("Enter the current time (24hr clock): "))
Enter the current time (24hr clock): 13
>>> 
>>> Hours_To_Wait = int(input("Hours to wait until alarm goes off: "))
Hours to wait until alarm goes off: 50
>>> 
>>> #Calculate
>>> Alarm_Time -  (Current_Time + Hours_ To_Wait) % 24
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> #Calculate
>>> Alarm_Time = (Current_Time + Hours_To_Wait) % 24
>>> 
>>> #Display Results
>>> 
>>> print(f"\nAlarm will go off at {Alarm_Time}:00")

Alarm will go off at 15:00
