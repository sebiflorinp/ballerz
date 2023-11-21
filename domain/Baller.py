class Baller:
	
	def __init__(self,_id_baller, _nume,_valoare):
		self.__id_baller = _id_baller
		self.__nume = _nume
		self.__valoare = _valoare

	def get_id_baller(self):
		return self.__id_baller

	def get_nume(self):
		return self.__nume
	
	def get_valoare(self):
		return self.__valoare
	
	def __eq__(self, other):
		return self.__id_baller == other.__id_baller