from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(employee):
    def calculate_salary(self):
        print(45_000)
class FullTimeEmployee(employee):
    def calculate_salary(self):
        print(100_000)
class ContractEmployee(employee):
    def calculate_salary(self):
        print(200_000)
intern1=Intern()
intern1.calculate_salary()
fulltimeemployee=FullTimeEmployee()
fulltimeemployee.calculate_salary()
contractemployee=ContractEmployee()
contractemployee.calculate_salary()

        
