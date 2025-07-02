# day2_input.py
# Day 2 - User input, type conversion, string formatting

name = input("Enter your name: ")
age = input("Enter your age: ")

# Convert age to integer
age = int(age)

print("Hello", name + "!")
print("Next year, you'll be", age + 1)

# Using f-string (modern way)
print(f"{name}, you will be {age + 1} years old next year.")
