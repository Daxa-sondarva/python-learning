class Dog:
    def sound(self):
        return "Bark 🐶"

class Cat:
    def sound(self):
        return "Meow 🐱"

class Lion:
    def sound(self):
        return "Roar 🦁"

class Elephant:
    def sound(self):
        return "Trumpet 🐘"

# Creating a list of different animal objects
animals = [Dog(), Cat(), Lion(), Elephant()]

# Using a loop to call the sound method polymorphically
for animal in animals:
    print(animal.sound())
