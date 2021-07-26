import unittest
from classes.Task import Task

class TestTaskClass(unittest.TestCase):
    """Test the Task Class"""
    def setUp(self):
        """Create an instance of the Task class for testing all class functions"""
        self.test_task = Task("Doing laundry", "15")

    def test_increase_time(self):
        """Tests increasing time by a set amount"""
        self.test_task.task_time = 15
        self.test_task.increase_time(5)
        self.assertEquals(self.test_task.task_time, 20)

    def test_increase_time_default(self):
        """Tests increasing time by the default amount of 1"""
        self.test_task.task_time = 15
        self.test_task.increase_time()
        self.assertEquals(self.test_task.task_time, 16)

    def test_decrease_time(self):
        """Tests decreasing time by a set amount"""
        self.test_task.task_time = 15
        self.test_task.decrease_time(5)
        self.assertEquals(self.test_task.task_time, 10)

    def test_decrease_time_default(self):
        """Tests increasing time by the default amount of 1"""
        self.test_task.task_time = 15
        self.test_task.decrease_time()
        self.assertEquals(self.test_task.task_time, 14)
    
    def test_reset_time(self):
        """Tests resetting the time to 0"""
        self.test_task.task_time = 15
        self.test_task.reset_time()
        self.assertEquals(self.test_task.task_time, 0)