class Bird:
    def speak(self):
        print("Birds make different sounds")

class Sparrow(Bird):
    #It overrides the speak() method.
    def speak(self):
        print("Chirp Chirp ")

class Parrot(Bird):
    #It overrides the speak() method.
    def speak(self):
        print("Squawk! ")

# Creating objects
bird1 = Sparrow()
bird2 = Parrot()

# Calling speak() - Polymorphism
bird1.speak()  # Output: Chirp Chirp 
bird2.speak()  # Output: Squawk! 
