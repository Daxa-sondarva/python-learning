# Parent class
class Vehicle:
    def vehicle_info(self):
        print(" This is a Vehicle")

# First Child class (inherits from Vehicle)
class Car(Vehicle):
    def car_info(self):
        print(" This is a Car")

# Second Child class (inherits from Vehicle)
class Bike(Vehicle):
    def bike_info(self):
        print(" This is a Bike")

# Another Child class (inherits from both Car and Bike)
class HybridCar(Car, Bike):
    def hybrid_car_info(self):
        print(" This is a Hybrid Car")

# Creating object of HybridCar
obj = HybridCar()

# Calling methods
obj.vehicle_info()  # Inherited from Vehicle
obj.car_info()      # Inherited from Car
obj.bike_info()     # Inherited from Bike
obj.hybrid_car_info()  # HybridCar's own method
