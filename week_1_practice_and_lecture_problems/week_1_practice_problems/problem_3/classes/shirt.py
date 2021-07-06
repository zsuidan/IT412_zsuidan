class Shirt():
    """A simple class for representing a shirt"""

    def __init__(self, size, color):
        """Initialize size and color attributes"""

        self.size = size
        self.color = color
    
    def getShirtInfo(self):
        """Prints out shirt attributes"""
        
        print("The size of the shirt is " + self.size)
        print("The color of the shirt is " + self.color)