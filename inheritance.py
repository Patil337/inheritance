class Car://( parent class created object)
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def show_details(self):
        print("name of car:",self.name)
        print("price of car:",self.price)
        print("color of car:",self.color)
c1=Car("ram",45000,"red")
c1.show_details()

class Vehicle(Car):// (child class created object)
    def show_model(self):
        print("execellent model")
v1=Vehicle("raj",42000,"blue")
v1.show_model()