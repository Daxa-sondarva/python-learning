''' tuple => tuple is a collection which is ordered and immutable (cannot be changed).
Tuples are used to store multiple items in a single variable.'''

#creating tuples
my_tuple = ('apple','banana','cherry')
t1 = (1, 2, 3)
t2 = ('a','b','c')
t3 = (1, 'hello', 3.5)
print(my_tuple,t1,t2,t3)

#Accessing Elements
fruits = ('apple','banana','cherry') 
print(fruits[1])   # Output: banana

'''Tuple Unpacking
This allows you to assign each item of a tuple to a variable in one line.'''
prog_lang = ("python","java","c++","go")
a,b,c,d = prog_lang
print(c) # Output: c++

#Tuple Operations
nums = (10,20,30,40,50)

print(len(nums))        # Length of tuple
print(30 in nums)       # Membership test
print(nums.index(20))   # Index of value
print(nums.count(10))   # Count of 10

# Tuple Slicing
letter = ('a','b','c','d','e')
print(letter[1:4]) # output : ('b','c','d')

#Nested Tuples
nested = ((1,2),(3,4),(5,6))
print(nested[1])    # Output: (3, 4)
print(nested[1][0]) # Output: 3

#Tuple as Dictionary Key (Immutable Required)
locations ={
    (22.3,88.4):"Kolkata",
    (19.0,72.8):"Mumbai"
}
print(locations[(22.3,88.4)]) #output : Kolkata

#unpaking 
student = ('daxa', 20, 'python')
name, age, fav_prog_lang =student
print(name)
print(age)
print(fav_prog_lang)

#Unpaking using function
def get_student_details():
    return ('daxa', 21, 'Python')
# Unpack the returned tuple
name,age,language = get_student_details()

print(f"My name is {name},I'am {age} year old and I love {language}.")