import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'taskscheduler'))
import taskscheduler as tsc


class Task_Scheduler(unittest.TestCase):
    def test_schedule_one_run(self):
            TaskLocation = "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe"
            TaskScheduledTimeForm = ['05','05','2020','11','01','00'] # will always need to change this manually
            FileName = "test2.exe"
            TaskName = "Test"

            TaskPid = tsc.schedule_one_run(TaskLocation,TaskScheduledTimeForm,FileName,TaskName)
            
            #testing to see if it is not running now
            Process = 'test2.exe'
            ProcessStatus = tsc.check_if_running(Process)

            time.sleep(60)

            # testing to see if it is now running
            Process2 = 'test2.exe'
            ProcessStatus2 = tsc.check_if_running(Process)

            self.assertEqual(ProcessStatus, False)
            self.assertEqual(ProcessStatus2, True)

if __name__ == "__main__":
    unittest.main()