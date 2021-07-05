from classes.clothing import Clothing

class ShirtInherit(Clothing):
    """A simple class for representing a shirt"""
    def __init__(self, size, color, sleeve_type, printed_message):
        """Initializes size, color, and quantity attributes from the clothing parent class and initializes new attributes for sleeve type and printed message"""
        super().__init__(size, color)
        self.sleeve_type = sleeve_type
        self.printed_message = printed_message

    def printMessage(self):
        """Prints the current message on the shirt"""
        print(self.printed_message)