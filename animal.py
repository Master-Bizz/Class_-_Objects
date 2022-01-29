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
 