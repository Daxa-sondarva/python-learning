#create set
fruits = {'apple','banana','cherry'}
print(fruits) #output: {'banana', 'apple', 'cherry'}

# No Duplicates Allowed
item = {'pen','book','pen','pencil'} #The duplicate 'pen' is removed automatically.
print(item) # output: {'pencil', 'pen', 'book'}

# Set Operations

A = {1,2,3,4}
B = {3,4,5,6}

#union
print("union : ",A.union(B)) #output : {1, 2, 3, 4, 5, 6}
print("intersecation : ",A.intersection(B)) #output : 3,4
print("Defference : ",A.difference(B)) #output:1,2

colors = {'red','blue','green','yellow','purple'}
print("colors : ",colors) #output : colors :  {'yellow', 'green', 'blue', 'red', 'purple'}

#Add an item to a set
colors.add('black')
print("Add New color : ",colors) #output :{'yellow', 'blue', 'green', 'purple', 'red', 'black'}

#Update set with multiple items
colors.update(['white','pink'])
print("Add 'white' and 'pink' to the colors set : ",colors)#output : {'yellow', 'blue', 'purple', 'white', 'pink', 'red', 'black'}

# Remove an item
colors.remove('green') # If "green" is not in the set, this will raise an error.
print("remove green form colors set : ",colors) #output : {'yellow', 'blue', 'purple', 'white', 'pink', 'red', 'black'}

# Discard an item
colors.discard('orange') # Won’t raise error if not found
print("discard 'Orange' : ",colors) #output :  {'yellow', 'blue', 'purple', 'white', 'pink', 'red', 'black'}


# Set Operations: Union, Intersection, Difference
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'mango', 'kiwi'}

# Union
print("Union:", set1.union(set2)) #output:Union: {'apple', 'cherry', 'kiwi', 'mango', 'banana'}

# Intersection
print("Intersection:", set1 & set2) #output:Intersection: {'cherry', 'banana'}

# Difference
print("Only in set1:", set1 - set2) #output:Only in set1: {'apple'}
print("Only in set2:", set2 - set1) #output:Only in set2: {'mango', 'kiwi'}


# Remove Duplicates from a List using Set
items = ['pen','pencil','book','pen','eraser','pencil']
unique_items = set(items)
print(unique_items) #output: {'pen', 'eraser', 'book', 'pencil'}

#Check if two sets are disjoint
a = {1, 2, 3}
b = {4, 5, 6}

print("Disjoint:", a.isdisjoint(b))  # output : True
