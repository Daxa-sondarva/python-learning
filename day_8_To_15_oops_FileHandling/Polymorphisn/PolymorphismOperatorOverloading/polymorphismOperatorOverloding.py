#operator overloding
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
     #  Overload -
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    #  Overload *
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    #  Overload ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    #  Overload print()
    def __str__(self):
        return f"({self.x}, {self.y})"
# Creating objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Adding objects (operator overloading)
p3 = p1 + p2
print(p3.x, p3.y)  # Output: 6 8
#also we cando like :
print("Addition:", p1 + p2)       #  (6, 8)
print("Subtraction:", p1 - p2)    #  (-2, -2)
print("Multiplication:", p1 * p2) #  (8, 15)
print("Equality:", p1 == p2)      #  False
print("Equality:", p1 == Point(2, 3))  #  True

print("Print p1:", p1)  #  (2, 3)
