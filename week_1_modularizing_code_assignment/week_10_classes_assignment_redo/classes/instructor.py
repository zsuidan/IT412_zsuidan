from classes.person import Person

class Instructor(Person):
    """A simple class for representing an instructor"""
    def __init__(self, name, email, id, institution_graduated_from, highest_degree_earned):
        super().__init__(name, email, id)
        self.institution_graduated_from = institution_graduated_from
        self.highest_degree_earned = highest_degree_earned

    def showInformation(self):
        """Prints out all information for a certain instructor"""
        print("Name: " + self.name.title() + " | Email: " + self.email + " | Instructor ID: " + self.id + " | Graduated from: " + self.institution_graduated_from.title() 
              + " | Degree earned: " + self.highest_degree_earned.title())
