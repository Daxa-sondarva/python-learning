#  Global Scope
x = "Global X"  # G

def outer():
    #  Enclosing Scope
    x = "Enclosing X"  # E
    
    def inner():
        #  Local Scope
        x = "Local X"  # L
        print("Inside inner():", x)

    inner()
    print("Inside outer():", x)

#  Built-in Function
print("Using built-in len():", len("Daxa"))  # B

# Call the outer function
outer()

# Accessing global variable
print("Outside all functions (Global):", x)
