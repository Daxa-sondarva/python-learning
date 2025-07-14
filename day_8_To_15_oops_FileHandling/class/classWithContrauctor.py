class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def show_details(self):
        return f" title : {title}, author :{author}, prive : {price}"


title = input("Enter a Title : ")
author = input("Enter a author : ")
price = float(input("Enter a Title : "))

obj=Book(title,author,price)

print(obj.show_details())
