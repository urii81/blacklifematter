from deck import Deck
from player import Player
import sys

class Partida:
	
	_players=[]
	_croupier= Player(1000000000000,"croupier")

	def __init__(self):
		self._baralla=Deck(6)
		self._players.append(self._croupier)
		self._magicPoints=0
	
	def get_baralla(self):
		return self._baralla.getdeck()

	def get_players(self):
		pl=[]
		for player in self._players:
			pl.append(str(player))
		return(pl)
	
	def hit(self,name):
		for player in self._players:
			if player.getName()== name:
					card=self._baralla.pick_a_card_from_deck()
					self._magicPoints+=self.check_magic_points(card)
					player.add_card_to_hand(card)
		print(self._magicPoints)

	def initialization(self):
		self._baralla.shuffle_deck("high")
		#do 2 times 
		for player in self._players:
			self.hit(player.getName())
		for player in self._players:
			self.hit(player.getName())
			#if player.getName == 'croupier':

	def add_player(self,pasta,name):
		player=Player(pasta,name)
		self._players.append(player)

    #def deal():
    #	hit
    #	hit(croupier)
	
	def checkWinner(self,player):
		#show dealer's second card
		#while dealer.points <17 : hit
		points1,points2=player.points()
		if (points1>21 or points2>21):
			player.set_status(False)
	
	def round(self):
		for player in self._players:
			if player.getName()!='croupier':
				print("PLAYER",player.getName() )
				print(" draw another card ¿?(Y or N)")
				choice=input()  
				while (choice =="Y"):
					self.hit(player.getName())
					self.checkWinner(player)
					if not player.get_status():
						print("Sorry you've lost")
						choice="N"
					print(" draw another card ¿?(Y or N)")
					choice=input()  


	def check_magic_points(self,card): # input: inspecting card
	    MP = 0 # magic points 
	    if (card.get_value() > 1 and card.get_value() < 7): # 2-6: +1
	        return 1
	    if (card.get_value() > 6 and card.get_value() < 10):
	    	return 0
	    else: # 10,11,12,13,1: 1
	        return -1
	    return (MP) # o: return total magic points 



partida1 = Partida()
partida1.add_player("100","Oriol")
partida1.initialization()
#partida1.hit("Oriol")
#print (partida1.get_baralla())
print("GET PLAYERS",partida1.get_players())
partida1.round()
print("GET PLAYERS",partida1.get_players())