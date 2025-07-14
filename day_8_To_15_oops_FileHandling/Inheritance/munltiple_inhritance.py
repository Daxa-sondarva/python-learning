class mom:
    def mom_method(self):
        print("mom class method")

class dad:
    def dad_method(self):
        print("dad class method")

# Child class inheriting Parent class
class child(mom,dad):
    def child_method(self):
        print("child class method")

# Creating an object of Child class
obj = child()
obj.mom_method()  # Accessing parent mom class method
obj.dad_method()  # Accessing parent dad class method
obj.child_method()  # Accessing child class method