from domain.Baller import Baller
class ServiceBallerz:
	def __init__(self,repo_ballerz,validator_baller):
		self.__repo_ballaz = repo_ballerz
		self.__validator_baller = validator_baller

	def top_3_ballaz(self):
		return sorted(self.__repo_ballaz.get_all(),key=lambda x:x.get_valoare(),reverse=True)[:3]

	def adauga_baller(self, id_baller, nume_baller, valoare):
		baller = Baller(id_baller,nume_baller,valoare)
		self.__validator_baller.valideaza(baller)
		self.__repo_ballaz.adauga_baller(baller)