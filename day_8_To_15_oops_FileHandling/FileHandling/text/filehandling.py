# import os

# print(os.getcwd())  # Prints the current working directory
# print(os.listdir())  # Lists all files in the current directory

#Opening a File
# file = open("example.txt", "r") 
file = open("FileHandling/text/example.txt", "r")  # "r" means read mode # Correct relative path
print(file.read())
file.close()

#Writing to a File
file = open("FileHandling/text/example.txt", "w")  
file.write("Hello, Python!")  
file.close()

#Reading from a File
file = open("FileHandling/text/example.txt", "r")  
content = file.read()  
print(content)  
file.close()

 #Best Practice: Using with Statement
with open("FileHandling/text/example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to manually close the file


