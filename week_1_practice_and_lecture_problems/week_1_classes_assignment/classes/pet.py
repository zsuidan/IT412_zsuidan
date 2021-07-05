class Pet():
    """A simple class for representing a pet"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clean(self):
        """Represents the act of cleaning the pet"""
        print(self.name + " is clean!")