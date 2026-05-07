class Vehicle:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
class car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
class bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc
car1=car("TATA","Z5",5)
print(car1.brand)
print(car1.model)
print(car1.seats)
bike1=bike("Honda","Shine",125)
print(bike1.brand)
print(bike1.model)
print(bike1.engine_cc)
