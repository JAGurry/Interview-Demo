import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'taskscheduler'))
import taskscheduler as tsc


class Task_Scheduler(unittest.TestCase):
    def test_run_immediately(self):
            TaskLocation = "C:\\Users\\jgurry\\ProjectCode\\PythonProjects\\Omitron Interview\\dist\\test2\\test2.exe"
            TaskPid = tsc.run_immediately(TaskLocation)
            Process = 'test2.exe'
            ProcessStatus = tsc.check_if_running(Process)

            self.assertTrue(ProcessStatus)


if __name__ == "__main__":
    unittest.main()