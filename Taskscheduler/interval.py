import sys
import taskscheduler as tsc
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os

PidFile = r'C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\PIDs.txt'
FileName = sys.argv[1]
TaskLocation = sys.argv[2]
TaskInterval = int(sys.argv[3])
TaskName = sys.argv[4]
Identifier = TaskInterval

# sheduling task run
sched = BackgroundScheduler(daemon=True) #configuring the scheduler
sched.add_job(tsc.check_and_run_int,'interval',seconds=TaskInterval, 
                id='myJobId',args=[FileName,TaskInterval, TaskLocation, TaskName])
sched.start() # starts the scheduler


TaskPid = os.getpid()
tsc.write_pid(TaskPid, TaskName, Identifier,PidFile)
while True:
    time.sleep(1)

