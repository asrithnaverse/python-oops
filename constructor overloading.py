class Person:
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Address: ",self.address)
person1=Person("Asrith")
person2=Person("Asrith",18)
person3=Person("Asrith",18,280)
person1.display()
person2.display()
person3.display()
