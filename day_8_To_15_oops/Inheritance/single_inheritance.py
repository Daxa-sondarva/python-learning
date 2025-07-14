class parent:
    def parent_method(self):
        print("Parent class method")

# Child class inheriting Parent class
class child(parent):
    def child_method(self):
        print("child class method")

# Creating an object of Child class
obj = child()
obj.parent_method()  # Accessing parent class method
obj.child_method()  # Accessing child class method