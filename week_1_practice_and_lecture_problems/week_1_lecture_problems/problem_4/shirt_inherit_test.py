from classes.clothing import Clothing
from classes.shirtinherit import ShirtInherit

another_shirt = ShirtInherit("M", "Black", "Long", "Python is neat")

another_shirt.increaseQuant(4)
print(another_shirt.quantity)

another_shirt.printMessage()