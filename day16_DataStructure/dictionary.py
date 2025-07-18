#Dictionary
my_dict = {
    "name": "Daxa",
    "age": 25,
    "language": "Python"
}
print(my_dict) #output : {'name': 'Daxa', 'age': 25, 'language': 'Python'}

#access value
student = {
    "name": "Daxa",
    "age": 22,
    "course": "Python DSA"
}

print(student["name"])   # Output: Daxa
print(student.get("age"))  # Output: 22

# Add / Update
student["email"] = "daxa@example.com"  # Add new
student["age"] = 23                    # Update

print(student) # output : {'name': 'Daxa', 'age': 23, 'course': 'Python DSA', 'email': 'daxa@example.com'}

#Delete or Remove a Key from Dictionary
#Using del
student = {"name": "Daxa", "age": 23, "course": "Python DSA"}
del student["age"]  # Removes 'age' key
print(student)

# Using .pop()
student = {"name": "Daxa", "age": 23, "course": "Python DSA"}
student.pop("course")  # Removes and returns 'course'
print(student)

# Loop Through a Dictionary
#Loop through keys
for key in student:
    print(key)

#Loop through value
for value in student.values():
    print(value)

#Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

#Check If Key Exists
if "name" in student:
    print("Name is available")

#Get Length of Dictionary
print(len(student))  # Number of key-value pairs

#Nested Dictionary
students = {
    "student1": {"name": "Daxa", "age": 23},
    "student2": {"name": "Raj", "age": 25}
}

print(students["student1"]["name"])  # Output: Daxa





#code with daxa sondarva in 2025
