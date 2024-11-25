class Car():
    def __init__(self,make, brand):
        self.__make=make
        self.brand=brand
        print("printing from car class")
    def get_make(self):
        return self.__make
    def set_make(self,make):
        self.__make=make

class BMW(Car):
    def __init__(self, price, make, brand):
        # super().__init__(make, brand)
        Car.__init__(self, make,brand)
        self.price=price
        print("printing from BMW class")

myCar = Car("2022","Maruti")
print(myCar.brand)
print(myCar.__dict__)

bmwCar =BMW(700000,"2023","some brand")
print(bmwCar.get_make())
print(bmwCar.price)
print(bmwCar.__dict__)

