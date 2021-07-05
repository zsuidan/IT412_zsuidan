from classes.pet import Pet
from classes.dog import Dog
from classes.cat import Cat

my_dog = Dog("Scout", 3, "German Shepard")
print("My dog's name is: " + my_dog.name)
my_dog.clean()
print("My Dog's breed is: " + my_dog.breed)

my_cat = Cat("Fluffy", 3)
print("My cat's name is: " + my_cat.name)