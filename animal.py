class Animal:
  # Initialize
 def __init__(self,name,age):
   # Instance Variable
   self.name = name
   self.age = age
  # Instance Method
 def speak(self):
       return f"My name is {self.name} and I am {self.age} years old."
 def intro(self):
           return f" The names {self.name}, {self.name} Bond."
 

class Shapes:
  def __init__(self,area,sides):
    self.area = area
    self.sides = sides
  def speak(self):
     return f"The Shape is {self.area}cm2 and has as many as {self.sides}."