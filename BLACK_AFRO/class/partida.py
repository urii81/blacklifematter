from deck import Deck

class Partida:
    def __init__(self):
        self._baralla=Deck(6)

    def get_baralla(self):
        return self._baralla
        

partida1 = Partida()
print (partida1.get_baralla)
