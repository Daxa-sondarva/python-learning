'''Python does not support traditional method overloading like other languages (Java, C++). 
That means you cannot define multiple methods with the same name but different arguments.'''

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c  # Third parameter is optional

# Creating object
calc = Calculator()

# Calling add() with 2 or 3 arguments
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9
