from pprint import pprint
class Card:
	_value=0
	_suit=""
	def __init__(self, value,suit):
		self._value=value
		self._suit=suit


	def get_suit():
		return self._suit
	def get_value():
		return self._value

	def __str__(self):
		return '{} {}'.format(self._value,self._suit)
	



