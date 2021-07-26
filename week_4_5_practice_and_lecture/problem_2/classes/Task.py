class Task():
    """Represents a task"""

    def __init__(self, task_description, task_time):
        """Constructor for Task class"""
        self.task_description = task_description
        self.task_time = task_time
    
    def increase_time(self, amount = 1):
        """Increases the task time for the Task by an entered amount, increasing by 1 if no amount is entered"""
        self.task_time = int(self.task_time) + amount

    def decrease_time(self, amount = 1):
        """Decreases the task time for the Task by an entered amount, decreasing by 1 if no amount is entered"""
        self.task_time = int(self.task_time) - amount

    def reset_time(self):
        """Resets the task time for the Task to 0"""
        self.task_time = 0