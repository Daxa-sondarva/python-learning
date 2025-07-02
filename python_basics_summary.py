# python_basics_summary.py
# A complete summary of basic Python topics

# 1. Variables and Data Types
name = "Daxa"
age = 24
height = 5.4
is_learning = True
print("\n Variables and Data Types")
print(name, age, height, is_learning)

# 2. User Input and Type Casting
print("\n User Input and Type Casting")
user_age = int(input("Enter your age: "))
print(f"Next year, you'll be {user_age + 1}")

# 3. If-Else Conditions
print("\n If-Else Conditions")
if user_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4. Loops
print("\n For Loop Example")
for i in range(1, 4):
    print("Loop count:", i)

print("\n While Loop Example")
count = 1
while count <= 3:
    print("While loop:", count)
    count += 1

# 5. Strings
print("\n String Methods")
message = " Hello Python "
print(message.strip().upper())

# 6. Lists
print("\n🟢 Lists")
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

# 7. Tuples
print("\n Tuples")
colors = ("red", "green", "blue")
print(colors[0])

# 8. Dictionaries
print("\n Dictionaries")
student = {"name": "Daxa", "age": 24, "city": "Rajkot"}
print(student["name"])

# 9. Sets
print("\n Sets")
unique_numbers = {1, 2, 3, 2}
unique_numbers.add(4)
print(unique_numbers)

# 10. Functions
print("\n Functions")
def greet(user):
    return f"Hello, {user}!"

print(greet("Daxa"))
