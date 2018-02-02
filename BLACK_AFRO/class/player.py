from script import *

#hola
class Player:
    def __init__(self):
        self._pocket = {0.5:1,1:0,2:0,5:0,10:0,20:0,50:0,100:0,500:0,1000:0}
    
    def get_pocket(self):
        pasta=0
        
        for i in self._pocket.keys():
            pasta+=(i*self._pocket[i])        
        return pasta

    def sum_pocket(self, money):
        self._pocket+=money


player1 = Player()
print(player1.get_pocket())
