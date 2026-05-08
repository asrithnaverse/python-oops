class Player:
    count=0
    def __init__(self):
        Player.count+=1
    @classmethod
    def display(cls):
        print(cls.count)
player1=Player()
player2=Player()
Player.display()
