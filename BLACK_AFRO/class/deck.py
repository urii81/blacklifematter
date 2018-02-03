import numpy as np
import  random as rand
from card import Card
class Deck:

    _suits=["hearts","diamonds","clovers","pikes"]
    _Num_suits = 4 # number of suits in a deck
    _outlist=[]
    _Num_cards = 52 # number of cards in a deck
    def __init__(self):
        pass

    def __init__(self,N_decks): # input:number of decks playing with
        self._N_decks=N_decks
        N_scards = self._N_cards/self._N_suits # number of cards in a suit
        Num_totalCards = self._N_cards*self._N_decks # number of total cards
            
        self._outlist = np.zeros((N_tcards),dtype=int) # declare output deck
        count = 0 # indexing array

        for suit in suits:
           for i in range(1,14):
            card=(i,suit)
            self._outlist.append(card)

    def getdeck(self):
        return self._outlist # output:ordenate deck


    def shuffle_deck(self,intensity): # input deck and low,medium,high
                                     # shuffle intensity
        N_tcards = len(self._outlist) # number of total cards in current deck

        if (intensity == 'low'): # if intensity low: 100 iterations

            it = 100

        elif (intensity == 'medium'): # else if intesity is medium then

            it = 1000

        else: # anything else: set intensity value to highest iterations 

            it = 10000
        
        for i in np.r_[0:it]: # do bucle 'it' times

            index1 = int((N_tcards-1)*rand.random()) # throw first rand int
            index2 = int((N_tcards-1)*rand.random()) # throw second rand
            memory = self._outlist[index1] # save first value in memory
            self._outlist[index1] = self._outlist[index2] # change positions
            self._outlist[index2] = memory 

            self._outlist = self._outlist[::-1] # reverse deck

        return (self._outlist) # output: shuffled deck 
'''
deck=Deck(6)
print(deck.getdeck())
deck.shuffle_deck('low')
print(deck.getdeck())
'''
