class Fruits:
    def __init__(self):
        print(f" Parent class Fruits constructor called from {self.__class__.__name__}")

    def fruits_method(self):
        print(f" Fruits method called from {self.__class__.__name__}")

class Banana(Fruits):
    def banana_method(self):
        print(f" Banana method called from {self.__class__.__name__}")

class Mango(Fruits):
    def mango_method(self):
        print(f" Mango method called from {self.__class__.__name__}")

class Kivi(Fruits):
    def kivi_method(self):
        print(f" Kivi method called from {self.__class__.__name__}")

class Strawberry(Fruits):
    def strawberry_method(self):
        print(f" Strawberry method called from {self.__class__.__name__}")

# Creating objects
print("Creating Banana object:")
banana = Banana()
banana.fruits_method()

print("\nCreating Mango object:")
mango = Mango()
mango.fruits_method()

print("\nCreating Kivi object:")
kivi = Kivi()
kivi.fruits_method()

print("\nCreating Strawberry object:")
strawberry = Strawberry()
strawberry.fruits_method()
