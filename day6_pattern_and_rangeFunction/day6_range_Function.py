# Common range() Variations with for loop

# 1 ) Print 0 to 4 (default start = 0)
for i in range(5):
    print(i) # output : 0,1,2,3,4

print("----------------")

# 2 ) Print 1 to 5
for i in range(1, 6):
    print(i) # output : 1,2,3,4,5

print("----------------")

# 3 ) Print even numbers from 2 to 10

print("enven numbers:")
for i in range(2, 11, 2):
    print(i) # output : 2,4,6,8,10

print("----------------")

# 4 ) Print numbers in reverse (10 to 1) 
print('reverse continue')
for i in range(10, 0, -1):
    print(i) # output : 10,9,8,7,6,5,4,3,2,1

print('range() with step  To skip or reverse numbers')
for i in range(1, 20, 3):
    print(i)



print("----------------")

# 5 ) Print all odd numbers from 1 to 20

print("odd numbers:")
for i in range(1, 21, 2):
    print(i) # output :1,3,5,7,9,11,13,15,17,19

print("----------------")


''' 6 ) Example with a string:
 range() with len() function-> When looping over strings or lists '''

text = "Python"
for i in range(len(text)):
    print("Index:", i, "Character:", text[i])


print("----------------")

# 7 ) Example with a list:
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print("Index:", i, "Fruit:", fruits[i])

print("----------------")



