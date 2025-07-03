# day5_conditionals.py

# Basic if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# if-elif-else chain
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

# Nested if
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Access granted!")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")
