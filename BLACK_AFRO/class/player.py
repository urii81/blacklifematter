
from deck import Deck
from card import Card

class Player:

	def __init__(self,_pocket,name):
		self._pocket ={0.5:1,1:0,2:0,5:0,10:0,20:0,50:0,100:0,500:0,1000:0}
		self._name=name
		self._ma=[]
		self._status=True

	def get_pocket(self):
		
		pasta=0

		for i in self._pocket.keys():
			pasta+=(i*self._pocket[i])        
		return pasta

	def sum_pocket(self, money):
		self._pocket+=money

	def getName(self):
		return self._name

	def add_card_to_hand(self,Card):
		self._ma.append(Card)

	def get_hand(self):
		return self._ma

	def points(self):

		points1=0
		points2=0
		has_ace=False
		for card in self._ma:

			if card.isAce():
				has_ace=True
			if (card.get_value()==11 or card.get_value()==12 or card.get_value()==13):
				points1+=10
			else:			
				points1+=card.get_value()
		if (has_ace and points1<=11):
			points2=points1+10

		return points1,points2
	def __str__(self):
		return '{} {}'.format(self._name,self._ma)




'''player1 = Player()
card1=Card('1','cors')
card2=Card('2','pikes')
player1.add_card_to_hand(card1)
player1.add_card_to_hand(card2)
print(player1.get_hand())
print(player1.points())'''