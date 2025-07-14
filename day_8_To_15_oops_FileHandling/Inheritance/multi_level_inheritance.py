class nani:
    def nani_method(self):
        print("nani class method")

class mom(nani):
    def mom_method(self):
        print("mom class method")


# Child class inheriting Parent class
class child(mom):
    def child_method(self):
        print("child class method")

# Creating an object of Child class
obj = child()
obj.nani_method()  # Accessing grandparent class method
obj.mom_method()   # Accessing parent class method
obj.child_method()  # Accessing child class method