# Python Functions

# 1 User Define functions

#Define a Function using def
def say_hello():
    print("Hello! Welcome to Python functions.")
say_hello() #Call a Function

print("-------------------")

#function defination
def fun( x ): 
    if (x % 2 == 0): 
        print("even")
    else: 
        print("odd")
  
fun(2) # function calling

print("---Parameterized Functions-----------")

'''Types of Users defined functions'''
# 1. Parameterized Functions
def fun(name):
    print("Hello,", name)

fun("Daxa") 

print("---Functions with default arguments-----------")


# 2. Functions with default arguments

# function definition:
def fun(x, y=50):  
    print("x:", x)  
    print("y:", y)  

fun(10)

print("---Keyword argument functions-----------")

# 3. Keyword argument functions
def fun(name, age):
    print(name, "is", age, "years old.")

fun(age=21, name="Daxa")

print("---Variable length argument functions-----------")

# 4. Variable length argument functions
# *args example
print("example of *args \n")
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   

# **kwargs example
print(f"example of **kwargs \n")
def fun(**kwargs):
    for k, val in kwargs.items():
        print( k,'=', val)

fun(a=1, b=2, c=3)

print("---Functions with Return value----------")

# 5. Functions with Return value

def fun(num):
    return num * num

# function calling
res = fun(5)
print(res)

print("---Lambda functions-----------")

# 6. Lambda functions
res = lambda x: x * x

print(res(4))

print("------")

# Pass by reference or Pass by value in Python
# Pass by reference (Immutable data types)
print("Pass by reference \n")
def fun(x):
    print("Value received:", x, "id:", id(x))

x = 12
print("Value passed:", x, "id:", id(x))
fun(x)
print("....................................")
#Pass by Reference (Mutable Data Types) 
print("Pass by Reference \n")
def fun(a):
    a[0] = 100  # Changing the first element of the list
    print("Inside function - lst:", a)

# Driver code
a = [1, 2, 3]  # List is mutable
print("Before function call - lst:", a)

# Function call
fun(a)

print("After function call - lst:",a)  # List is modified outside the function