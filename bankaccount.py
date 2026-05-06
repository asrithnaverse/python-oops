class BankAccount:
    def __init__(self,name,balance,accno):
        self.name=name
        self.balance=balance
        self.accno=accno
    def dep_money(self,depmoney):
        self.balance=self.balance+depmoney
        print(f"Deposited money= {depmoney}")
    def with_draw(self,withdraw_money):
        self.balance=self.balance-withdraw_money
        print(f"Money withdrawn={withdraw_money}")
    def get_balance(self):
        print(f"Balance={self.balance}")
    
user1=BankAccount("Asrith",10000,5031)
user1.with_draw(7000)
user1.dep_money(5000)
user1.get_balance()
