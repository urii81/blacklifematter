from deck import Deck
from player import Player
class Partida:
	
	_players=[]
	_croupier= Player(1000000000000,"croupier")

	def __init__(self):
		self._baralla=Deck(6)
		self._players.append(self._croupier)
	
	def get_baralla(self):
		return self._baralla.getdeck()
	
	#def hit(player):
		#_player1.add_card_to_hand(self._baralla.pick_a_card_from_deck())

	#def initialization(self):
		#do 2 times 
		#for player in players:
			#hit(player)
			#if player.getName == 'croupier':

	def add_player(self,name,pasta):
		player=Player(pasta,name)
		self._players.add(player)

    #def deal():
    #	hit
    #	hit(croupier)
	
	def checkWinner(self):
		#show dealer's second card
		#while dealer.points <17 : hit
		#
	def round(self):
		for player in players:
			if player.getName()!='croupier':
			print(" draw another card ¿?(Y or N)")
			choice=raw_imput()  
			if choice =="Y":
				hit(player)   
partida1 = Partida()
print (partida1.get_baralla())
