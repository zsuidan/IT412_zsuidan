from classes.person import Person

class Student(Person):
    """A simple class for representing a student"""
    def __init__(self, name, email, id, program_of_study):
        super().__init__(name, email, id)
        self.program_of_study = program_of_study

    def showInformation(self):
        """Prints out all information for a certain student"""
        print("Name: " + self.name.title() + " | Email: " + self.email + " | Student ID: " + self.id + " | Program of study: " + self.program_of_study.title())