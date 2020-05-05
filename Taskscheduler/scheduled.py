import sys
import taskscheduler as tsc
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import os


PidFile = r'C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\PIDs.txt'
FileName = sys.argv[1]
TaskLocation = sys.argv[2]
TaskScheduledTimeForm = sys.argv[3]
TaskName = sys.argv[4]
# converting back to date and time format
month = TaskScheduledTimeForm[:2]
day = TaskScheduledTimeForm[2:4]
year = TaskScheduledTimeForm[4:8]
hour = TaskScheduledTimeForm[8:10]
minute = TaskScheduledTimeForm[10:12]
second = TaskScheduledTimeForm[12:]
Identifier = '{}/{}/{} {}:{}:{} EST'.format(month,day,year,hour,minute,second)


# scheduling task run
sched = BackgroundScheduler(daemon=True) #configuring scheduler
sched.add_job(tsc.check_and_run_sched, 'date', 
                run_date=datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)), 
                args=[FileName, TaskName, TaskLocation]) #setting the schedule
sched.start()

TaskPid = os.getpid()
tsc.write_pid(TaskPid, TaskName, Identifier,PidFile)
while True:
    time.sleep(1)