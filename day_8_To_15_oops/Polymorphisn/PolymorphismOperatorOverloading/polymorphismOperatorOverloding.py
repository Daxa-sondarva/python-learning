class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Adding objects (operator overloading)
p3 = p1 + p2
print(p3.x, p3.y)  # Output: 6 8
