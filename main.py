import this

#=============================
from animal import Animal            # ( From animal.py import the 'Class' Animal)
print(dir(Animal))

# Creating instance/object
dog = Animal(name='Dizzy',age= 12)
cat = Animal(name='Izzy',age= 14)
lion = Animal(name='Samuel',age= 10)
print(dog.speak())
print(cat.speak())
print(lion.speak())

print(dog.intro())
print(cat.intro())
print(lion.intro())

from animal import Shapes

Hexagon = Shapes(area = 35, sides = 6)
Rectangle = Shapes(area = 28, sides = 4)

print(Hexagon.speak())
print(Rectangle.speak())
