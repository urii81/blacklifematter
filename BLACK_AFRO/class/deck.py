import numpy as np
import  random as rand
from card import Card
class Deck:

    _suits=["hearts","diamonds","clovers","pikes"]
    _Num_suits = 4 # number of suits in a deck
    _Num_cards = 52 # number of cards in a deck
    def __init__(self):
        pass

    def __init__(self,N_decks): # input:number of decks playing with
        self._outlist=[]
        self._N_decks=N_decks
        Num_totalCards = self._Num_cards*self._N_decks # number of total cards
        N_scards = Num_totalCards/self._Num_suits # number of cards in a suit
        

        for suit in self._suits:
           for i in range(1,14):
                card=Card(i,suit)
                self._outlist.append(card)
        self._outlist=self._outlist*N_decks

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

    def pick_a_card_from_deck(self): #input:deck with N cards

        picked_card = self._outlist[0] # pick the first card
        del(self._outlist[0]) # delete this card from deck

        #return (picked_card,self._outlist) # o: p-c and new deck with N-1 cards   
        return (picked_card)
    def __str__(self):
        for card in self._outlist:
            return  '{} {}'.format(card.get_value(),card.get_suit())
    

'''deck=Deck(6)
print(type(deck.getdeck()))
print("leeeeeeeeeen",len(deck.getdeck()))
deck.shuffle_deck('low')
print(deck.getdeck())
card,deck=deck.pick_a_card_from_deck()
print(card)
print("new deck",deck)'''

