from pprint import pprint
class Card:
	_value=0
	_suit=""
	def __init__(self, value,suit):
		self._value=int(value)
		self._suit=suit


	def get_suit(self):
		return self._suit
	def get_value(self):
		return self._value

	def isAce(self):
		return self._value==1

	def __repr__(self):
		return '{} {}'.format(self._value,self._suit)
	



