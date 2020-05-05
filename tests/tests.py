import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'taskscheduler'))
import taskscheduler as tsc


class Task_Scheduler(unittest.TestCase):
    def test_get_json(self):
        ConfigFile = r'C:\Users\jgurry\ProjectCode\PythonProjects\Omitron Interview\tests\test_config.json'
        TaskName = "Important Task"
        TaskData = tsc.get_json(TaskName, ConfigFile)
        TestDict = {"task_name": "Important Task",
                    "task_location": "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe",
                     "task_interval": 15, "task_scheduled_time": "", "task_scheduled": "false"}

        self.assertIsInstance(TaskData, list)
        self.assertGreater(len(TaskData), 0)
        self.assertDictEqual(TestDict, TaskData[0])


    def test_get_filename(self):
        TaskLocation = "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe"
        FileName = tsc.get_filename(TaskLocation)

        self.assertIsInstance(FileName, str)
        self.assertEqual(FileName, 'test2.exe')

    
    def test_check_if_running(self):
        # test of a process that should be True
        Process = 'chrome.exe'
        ProcessStatus = tsc.check_if_running(Process)

        # test of a process that should be False
        Process2 = 'chrome.diy'
        ProcessStatus2 = tsc.check_if_running(Process2)

        self.assertTrue(ProcessStatus)
        self.assertFalse(ProcessStatus2)
    """
    def test_run_immediately(self):
        TaskLocation = "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe"
        TaskPid = tsc.run_immediately(TaskLocation)
        Process = 'test2.exe'
        ProcessStatus = tsc.check_if_running(Process)

        self.assertTrue(ProcessStatus)


    def test_schedule_one_run(self):
        TaskLocation = "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe"
        TaskScheduledTimeForm = ['05','05','2020','02','18','00'] # will always need to change this manually
        FileName = "test2.exe"
        TaskName = "Test"

        TaskPid = tsc.schedule_one_run(TaskLocation,TaskScheduledTimeForm,FileName,TaskName)
        
        #testing to see if it is not running now
        Process = 'test2.exe'
        ProcessStatus = tsc.check_if_running(Process)

        time.sleep(65)

        # testing to see if it is now running
        Process2 = 'test2.exe'
        ProcessStatus2 = tsc.check_if_running(Process)

        self.assertFalse(ProcessStatus2)
        self.assertTrue(ProcessStatus2)
    """
    def test_time_format(self):
        TaskScheduledTimeRaw = "03/16/2020 04:00:00 EST"
        DateTest = tsc.time_format(TaskScheduledTimeRaw)

        self.assertIsInstance(DateTest, list)
        self.assertEqual(DateTest, ['03', '16', '2020', '04', '00', '00'])

    def test_kill_process_pid(self):
        # this will have to be changed every test
        # start by opening NotePad and finding the PID in the details Tab of the Task Manager
        TaskPid = 6992
        tsc.kill_process_pid(TaskPid)

        Process = 'notepad.exe'
        ProcessStatus = tsc.check_if_running(Process)

        self.assertFalse(ProcessStatus)



if __name__ == "__main__":
    unittest.main()