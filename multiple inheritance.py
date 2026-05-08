class Herbivore:
    def __init__(self,greenveg):
        self.greenveg=greenveg
class carnivore:
    def __init__(self,meat):
        self.meat=meat
class omnivore:
    def __init__(self,both):
        self.both=both
class Bear(Herbivore,carnivore,omnivore):
    def __init__(self,greenveg,meat,both,food):
        super().__init__(greenveg)
        carnivore.__init__(self,meat)
        omnivore.__init__(self,both)
        self.food=food
bear1=Bear("mint","chicken","egg","omlet")
print(bear1.greenveg)
print(bear1.meat)
print(bear1.both)
print(bear1.food)
