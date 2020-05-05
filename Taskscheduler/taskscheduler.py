import json
import psutil
import subprocess
import time
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

# loads and parses json file for data relevant to the specified task
def get_json(TaskName, ConfigFile):

    with open(ConfigFile) as f:
        FileData = json.load(f)

    TaskData = []
    for task in FileData['task_config']:
        if task['task_name'] == TaskName:
            TaskData.append(task)

    return TaskData


# saves the filename to a variable after parsing the file path
def get_filename(TaskLocation):
    FileName = TaskLocation.split('\\')[-1]

    return FileName


# checks if a program is running
def check_if_running(Process):
    ProcessStatus = Process in (p.name() for p in psutil.process_iter())

    return ProcessStatus


# runs the task once and immediately.
def run_immediately(TaskLocation):
    
    Process = subprocess.Popen([TaskLocation])
    Pid = os.getpid()
    time.sleep(5)
    return Pid
    sys.exit()


def schedule_one_run(TaskLocation,TaskScheduledTimeForm,FileName,TaskName):
    FilePath = r"C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\Taskscheduler\scheduled.py"
    Process = subprocess.Popen(["python", FilePath, FileName, TaskLocation, TaskScheduledTimeForm, TaskName, "&"])
    Pid = os.getpid()
    time.sleep(5)
    return Pid


# formats time from config file to meet format of apscheduler
def time_format(TaskScheduledTimeRaw):
    DateTimeList = TaskScheduledTimeRaw.split(" ")[:2]
    DateList = DateTimeList[0].split("/") 
    TimeList = DateTimeList[1].split(":")
    TaskScheduledTimeForm = DateList + TimeList
    return TaskScheduledTimeForm


# for one time executions that are scheduled
# combination of the run immediately and the status check
def check_and_run_sched(FileName, TaskName, TaskLocation):
    TaskStatus = check_if_running(FileName)
    if TaskStatus == True:
        print('Task: {} is already running. It cannot be run again.'.format(TaskName))
        print('To run process now input: python stop.py {} and rerun'.format(TaskName))
    else:
        print('Running Task: {} Shortly...\n'.format(TaskName))
        TaskPid = run_immediately(TaskLocation) 
        return TaskPid


# for an interval run option
# combination of the run immediately and the status check
def check_and_run_int(FileName,TaskInterval, TaskLocation, TaskName):
    TaskStatus = check_if_running(FileName)
    if TaskStatus == True:
        print('Task: {} is already running. It cannot be run again.'.format(TaskName))
        print('To run process now input: python stop.py {} and rerun'.format(TaskName))
    else:
        print('Running Task: {} every {} seconds\n'.format(TaskName, TaskInterval))
        TaskPid = run_immediately(TaskLocation) 
        return TaskPid


# schedules an interval run option
def schedule_interval(TaskLocation,TaskInterval,FileName,TaskName):
    FilePath = r"C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\Taskscheduler\interval.py"
    Process = subprocess.Popen(["python", FilePath, FileName, TaskLocation, str(TaskInterval), TaskName, "&"])
    TaskPid = os.getpid()
    time.sleep(5)
    return TaskPid


# kills a running task that is not scheduled or an interval
def kill_process(Process, TaskName):
    for p in psutil.process_iter(['name']):  # iterates through all processes
        ProcessName = p.info['name']
        if ProcessName == Process:
            p.kill()
    print('Task: {} has been killed'.format(TaskName))


# writes the pid to a file
def write_pid(TaskPid, TaskName, Identifier, PidFile):
    WriteTime = datetime.now()

    with open(PidFile, "a") as f:
        f.write('{},{},{},{}\n'.format(TaskName, WriteTime, Identifier, TaskPid))


# reads the pid file for the desired pid
def read_pid(TaskName, Identifier, PidFile):
    FileData =[]
    with open(PidFile, "r") as f:
        for line in f:
            DataList = line.split(",")
            DataDictionary = {'TaskName': DataList[0],'WriteTime': DataList[1], 
                                'Identifier': DataList[2], 'TaskPid': DataList[3] }
            FileData.append(DataDictionary)
    
    return FileData


# parses data collected from PID file and finds corect PID
def get_pid(TaskName, Identifier, FileData):

    for data in FileData:
        if data['TaskName'] == TaskName:
            TaskPid = data['TaskPid']
            return TaskPid
        else:
            print('Cannot Kill the Process. PID is unavailable')
            print('Use Task Manager to Kill python.exe')
            sys.exit()
            

# Kills process that requires PID: scheduled or interval process
def kill_process_pid(TaskPid):
    KillCommand = "taskkill /F /PID " + str(TaskPid)
    os.system(KillCommand)