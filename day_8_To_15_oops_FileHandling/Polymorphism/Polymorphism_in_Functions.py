class Dog:
    def sound(self):
        return "Dog - Bark"

class Cat:
    def sound(self):
        return "Cat - Meow"

class Lion:
    def sound(self):
        return "Lion - Roar"

class Elephant:
    def sound(self):
        return "Elephant - Trumpet"

# Creating a list of different animal objects
animals = [Dog(), Cat(), Lion(), Elephant()]

# Using a loop to call the sound method polymorphically
for animal in animals:
    print(animal.sound())
