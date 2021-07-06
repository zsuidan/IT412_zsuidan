class Clothing():
    """A simple class for representing a piece of clothing"""
    def __init__(self, size, color):
        """Initialize size, color, and quantity attributes with a default of 1 for quantity"""
        self.size = size
        self.color = color
        self.quantity = 1
    
    def decreaseQuant(self, quant):
        """Decreases the quantity by an inputted amount"""
        self.quantity -= quant

    def getClothingInfo(self):
        """Prints out clothing attributes"""
        print("The size of the clothing is " + self.size)
        print("The color of the clothing is " + self.color)

    def increaseQuant(self, quant):
        """Increases the quantity by an inputted amount"""
        self.quantity += quant