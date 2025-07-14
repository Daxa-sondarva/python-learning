from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):  
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (no implementation)

# Concrete class (child class)
class Dog(Animal):  
    def make_sound(self):  
        return "Bark"

class Cat(Animal):  
    def make_sound(self):  
        return "Meow"

# Trying to create an object of an abstract class (this will give an error)
# animal = Animal()  #  ERROR: Can't instantiate abstract class

# Creating objects of concrete classes
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark 
print(cat.make_sound())  # Output: Meow 
