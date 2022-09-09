from hashlib import new


class AlarmClock:

    def __init__(self):
        self.current_time = 1200
        self.is_on = False
        self.alarm_time = 0

    def setCurrentTime(self,getNewTime):
        self.current_time = getNewTime
        print (f"The time is now {self.current_time}.")

    def setAlarmTime(self, newAlarmTime):
        self.alarm_time = newAlarmTime
        print(f"Your alarm is now set for {self.setAlarmTime}.")
    
    def toggleAlarm(self):
        if self.is_on == True:
            self.is_on == False
            print("The alarm is now off!")
        elif self.is_on == False:
            self.is_on == True
            print("The alarm is now on!")
    
