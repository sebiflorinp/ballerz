from exceptii.RepoError import RepoError
class RepoBallerz:
	def __init__(self):
		self.__elems = {}

	def __len__(self):
		return len(self.__elems)
	
	def isEmpty(self):
		return len(self.__elems)==0

	def adauga_baller(self, baller):
		if baller.get_id_baller() in self.__elems:
			raise RepoError("id baller existent!\n")
		self.__elems[baller.get_id_baller()] = baller

	def cauta_baller_dupa_id(self, id_baller):
		if id_baller not in self.__elems:
			raise RepoError("id baller inexistent!\n")
		return self.__elems[id_baller]

	def get_all(self):
		return [self.__elems[id_baller] for id_baller in self.__elems]

	def modifica_baller(self, other_baller):
		id_baller = other_baller.get_id_baller()
		if id_baller not in self.__elems:
			raise RepoError("id baller inexistent!\n")
		self.__elems[id_baller] = other_baller

	def sterge_baller(self, id_baller):
		if id_baller not in self.__elems:
			raise RepoError("id baller inexistent!\n")
		del self.__elems[id_baller]
		
	