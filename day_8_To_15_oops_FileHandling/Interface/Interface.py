from abc import ABC, abstractmethod

# Defining an Interface
class Vehicle(ABC):  
    @abstractmethod
    def start_engine(self):
        pass  # No implementation

    @abstractmethod
    def stop_engine(self):
        pass  # No implementation

# Implementing the Interface in Car class
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started "

    def stop_engine(self):
        return "Car engine stopped "

# Implementing the Interface in Bike class
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started "

    def stop_engine(self):
        return "Bike engine stopped "

# car = Vehicle()  #  ERROR: Cannot instantiate an abstract class
car = Car()
bike = Bike()

print(car.start_engine())  #  Car engine started 
print(bike.start_engine())  #  Bike engine started 
