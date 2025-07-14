# Pattern Printing with Loops (using *)

# 1. Print a Right-Angled Triangle (* pattern)
# rows = int(input("Enter number of rows: "))
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

print("-----------------------")

#  2. Print a Number Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("-----------------------")

# 3. Reverse Star Pattern
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

print("-----------------------")

# 3. Solid Rectangle
print("Solid Rectangle")
rows = 4
cols = 6
for i in range(rows):
    print("*" * cols)

print("-----------------------")

# 4. Heart Shape with Stars
print("It's My Heart")
print("")
for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3 != 0) or 
            (row == 1 and col % 3 == 0) or 
            (row - col == 2) or 
            (row + col == 8)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("-----------------------")

# 5. Hollow Square
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")


print("-----------------------")


#“D” in Stars (Initial Style)
rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0 or (j == cols - 1 and i != 0 and i != rows - 1) or \
           ((i == 0 or i == rows - 1) and j < cols - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



            