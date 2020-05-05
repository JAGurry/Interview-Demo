import sys
import taskscheduler as tsc


TaskName = sys.argv[1]
ConfigFile = r'C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\configs\config.json'
PidFile = r'C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\PIDs.txt'

# load and parse json file for data relevant to the specified task
TaskData = tsc.get_json(TaskName, ConfigFile)
TaskNumber = len(TaskData)

# Check to see if the task exists in the config file 
if TaskNumber == 0:
    print('Task Was Not Found in Configuration File {}'.format(ConfigFile))
    sys.exit() 

TaskLocation = TaskData[0]['task_location']
FileName = tsc.get_filename(TaskLocation)
TaskScheduled = TaskData[0]['task_scheduled']
TaskInterval = TaskData[0]['task_interval']


# checking to see if the task is to be sheduled or run immediately
# and checking to see if it is to be run on an interval
if TaskScheduled == "true":
    TaskScheduledTimeRaw = TaskData[0]['task_scheduled_time']
    TaskScheduledTimeForm = tsc.time_format(TaskScheduledTimeRaw)
    if TaskInterval == 0:
        print('Scheduling Task: {} to run at {}'. format(TaskName, TaskScheduledTimeRaw))
        TaskPid = tsc.schedule_one_run(TaskLocation,TaskScheduledTimeForm,FileName,TaskName)

elif TaskScheduled == "false":
    if TaskInterval > 0:    
        TaskPid = tsc.schedule_interval(TaskLocation,TaskInterval,FileName,TaskName)
    elif TaskInterval == 0:
        TaskStatus = tsc.check_if_running(FileName)   # cheking if task is already running
        if TaskStatus == True:
            print('Task: {} is already running. It cannot be run again.'.format(TaskName))
            print('To run process now input: python stop.py {} and rerun'.format(TaskName))  
        else:
            print('Running Task: {} Shortly...\n'.format(TaskName))
            TaskPid = tsc.run_immediately(TaskLocation)        # running task

    




