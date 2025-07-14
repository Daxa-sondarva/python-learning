class fruits:
    def fruits_method(self):
        print("fruit method")


class Banana(fruits):
    def banana_method(self):
        print("banana method")

class Mango(fruits):
    def mango_method(self):
        print("mango method")

class Kivi(fruits):
    def kivi_method(self):
        print("kivi method")

class Stroberry(fruits):
    def stroberry_method(self):
        print("stroberry method")



banana = Banana()
banana.fruits_method()
banana.banana_method()

mango = Mango()
mango.fruits_method()
mango.mango_method()

kivi =Kivi()
kivi.fruits_method()
kivi.kivi_method()

stroberry = Stroberry()
stroberry.fruits_method()
stroberry.stroberry_method()
