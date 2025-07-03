#Maximum of Three Numbers

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("Max is", a)
elif b >= a and b >= c:
    print("Max is", b)
else:
    print("Max is", c)
