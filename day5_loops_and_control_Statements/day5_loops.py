# Print numbers from 1 to 5

# for loop
for i in range(1, 6):
    print(i)

print("----------------------------------------")

# while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

print("----------------------------------------")

# examples with else 
#for loop
for i in range(3):
    print("Loop:", i)
else:
    print("Loop finished successfully!")

print("----------------------------------------")

#while loop
x = 0
while x < 3:
    print("x is:", x)
    x += 1
else:
    print("Done looping.")
    
print("----------------------------------------")

# break and continue
# break

for i in range(1, 6):
    if i == 3:
        break #break = Exit the loop early
    print(i)

print("----------------------------------------")

# continue
for i in range(1, 6):
    if i == 3:
        continue #continue = Skip current iteration
    print(i)

print("----------------------------------------")

#Practice Exercises

#Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print("even number : ",i)


print("----------------------------------------")

#Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum is:", total)



