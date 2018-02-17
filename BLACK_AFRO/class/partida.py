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

	def get_players(self):
		pl=[]
		for player in self._players:
			pl.append(str(player))
		return(pl)
	
	def hit(self,name):
		for player in self._players:
			if player.getName()== name:
					player.add_card_to_hand(self._baralla.pick_a_card_from_deck())

	def initialization(self):
		#do 2 times 
		for player in self._players:
			hit(player.getName())
		for player in self._players:
			hit(player.getName())
			#if player.getName == 'croupier':

	def add_player(self,pasta,name):
		player=Player(pasta,name)
		self._players.append(player)

    #def deal():
    #	hit
    #	hit(croupier)
	
	#def checkWinner(self):
		#show dealer's second card
		#while dealer.points <17 : hit
		#
	def round(self):
		for player in players:
			if player.getName()!='croupier':
				print("PLAYER",player.getName() )
				print(" draw another card ¿?(Y or N)")
				choice=raw_imput()  
				if choice =="Y":
					hit(player.getName())   



partida1 = Partida()
partida1.add_player("100","Oriol")
partida1.initialization()
#partida1.hit("Oriol")
#print (partida1.get_baralla())
print(partida1.get_players())
