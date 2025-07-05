''' How to get function name in Python '''

# Method 1:  function.__name__

#This function has been introduced in Python 3 in Python3.
# initializing function
def DAXA():
   return "You just called for success !!"
# printing function name
# using function.__name__
print("The name of function is : " + DAXA.__name__)

print("------")
# Method 2: function.func_name 

# initializing function
'''def DAXA():
    return "You just called for success !!"'''

# printing function name
# using function.func_name
'''print("The name of function is : " + DAXA.func_name)''' # it will give me error becouse of its drawback and the drawback is that this works just for Python2.

print("------")

# Method 3:  __qualname__ attribute
def Daxa():
    pass

class Daxa(object):
    def my_method(self):      
        pass

# "my_function"
print(Daxa.__qualname__)    
# "My_Class.my_method"
print(Daxa.my_method.__qualname__)

print("------")
#Method 4: Get Function Name in Python using  the inspect module
import inspect
# initializing function
def my_function_name():
    # get the frame object of the function
    frame = inspect.currentframe()
    return frame.f_code.co_name
# printing function name
print("The name of function is : " +my_function_name()) # test_function
#This code is contributed by Edula Vinay Kumar Reddy