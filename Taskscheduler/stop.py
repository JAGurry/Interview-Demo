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
    Identifier = TaskScheduledTimeRaw 
    print(Identifier)
    print(TaskName)
    FileData = tsc.read_pid(TaskName, Identifier, PidFile)
    print(FileData)
    TaskPid = tsc.get_pid(TaskName, Identifier, FileData)
    tsc.kill_process_pid(TaskPid)
    print('Task: {} has been killed'.format(TaskName))

elif TaskScheduled == "false":
    if TaskInterval > 0:
        Identifier = str(TaskInterval)
        FileData = tsc.read_pid(TaskName, Identifier, PidFile)
        TaskPid = tsc.get_pid(TaskName, Identifier, FileData)
        tsc.kill_process_pid(TaskPid)
        print('Task: {} has been killed'.format(TaskName))  
    elif TaskInterval == 0:
        tsc.kill_process(FileName, TaskName)