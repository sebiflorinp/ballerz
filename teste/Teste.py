from domain.Baller import (Baller)
from validare.validator_baller import ValidatorBaller
from exceptii.ValidError import ValidError
from exceptii.RepoError import RepoError
from infrastructura.repo_ballerz import RepoBallerz
from business.ServiceBalllerz import ServiceBallerz
class Teste:
	def __init__(self):
		pass

	def ruleaza_toate_testele(self):
		self.__ruleaza_teste_domain()
		self.__ruleaza_teste_validare()
		self.__ruleaza_teste_infrastructura()
		self.__ruleaza_teste_business()

	def __ruleaza_teste_domain(self):
		print("start teste domain")
		id_baller = 23
		nume_baller = "Jordan"
		valoare = 9000.1
		baller = Baller(id_baller,nume_baller,valoare)
		assert id_baller == baller.get_id_baller()
		assert nume_baller == baller.get_nume()
		assert abs(valoare-baller.get_valoare())<0.00001
		print("teste domain terminate cu succes")

	def __ruleaza_teste_validare(self):
		print("start teste validare")
		id_baller = 23
		nume_baller = "Jordan"
		valoare = 9000.1
		baller = Baller(id_baller,nume_baller,valoare)

		id_baller_bad = -23
		nume_baller_bad = ""
		valoare_bad = -9000.1
		bad_balla = Baller(id_baller_bad,nume_baller_bad,valoare_bad)
		
		validator_baller = ValidatorBaller()
		validator_baller.valideaza(baller)
		
		try:
			validator_baller.valideaza(bad_balla)
			assert False
		except ValidError as ve:
			assert str(ve)=="id invalid!\nnume invalid!\nvaloare invalida!\n"


		print("teste validare terminate cu succes")

	def __ruleaza_teste_infrastructura(self):
		print("start teste repository ballerz")
		id_baller = 23
		nume_baller = "Jordan"
		valoare = 9000.1
		baller = Baller(id_baller,nume_baller,valoare)
		repo_ballaz = RepoBallerz()
		assert repo_ballaz.isEmpty()
		repo_ballaz.adauga_baller(baller)
		assert len(repo_ballaz)==1
		baller_gasit = repo_ballaz.cauta_baller_dupa_id(id_baller)
		assert baller_gasit == baller
		assert baller_gasit.__eq__(baller)
		assert baller_gasit.get_nume()==baller.get_nume()
		id_baller = 23
		nume_baller = "LeBum"
		valoare = 8000.1
		other_baller = Baller(id_baller,nume_baller,valoare)
		try:
			repo_ballaz.adauga_baller(other_baller)
			assert False
		except RepoError as re:
			assert str(re)=="id baller existent!\n"
		id_baller = 24
		nume_baller = "Kobe"
		valoare = 9000.05
		other_baller = Baller(id_baller,nume_baller,valoare)
		repo_ballaz.adauga_baller(other_baller)
		assert len(repo_ballaz)==2
		ballerz = repo_ballaz.get_all() 
		assert len(ballerz)==2
		ballerz.sort(key=lambda x: x.get_id_baller())
		assert ballerz[0]==baller
		assert ballerz[1]==other_baller
		id_baller = 23
		nume_baller = "LeBum"
		valoare = 8000.1
		other_baller = Baller(id_baller,nume_baller,valoare)

		repo_ballaz.modifica_baller(other_baller)
		baller_gasit = repo_ballaz.cauta_baller_dupa_id(id_baller)
		assert baller_gasit.get_nume()==other_baller.get_nume()
		repo_ballaz.sterge_baller(id_baller)
		assert len(repo_ballaz)==1
		try:
			repo_ballaz.sterge_baller(id_baller)
			assert False
		except RepoError as re:
			assert str(re)=="id baller inexistent!\n"
		try:
			repo_ballaz.modifica_baller(other_baller)
			assert False
		except RepoError as re:
			assert str(re)=="id baller inexistent!\n"






		print("teste repository ballerz terminate cu succes")

	def __ruleaza_teste_business(self):
		print("start teste business")
		repo_ballaz = RepoBallerz()
		validator_baller = ValidatorBaller()
		srv_ballaz = ServiceBallerz(repo_ballaz,validator_baller)
		id_baller = 24
		nume_baller = "Kobe"
		valoare = 9000.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		id_baller = 77
		nume_baller = "Luka"
		valoare = 7000.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		id_baller = 30
		nume_baller = "Curry"
		valoare = 8900.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		id_baller = 7
		nume_baller = "A.I."
		valoare = 7700.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		id_baller = 32
		nume_baller = "Dirk"
		valoare = 7300.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		id_baller = 33
		nume_baller = "Bird"
		valoare = 8800.05
		srv_ballaz.adauga_baller(id_baller,nume_baller,valoare)
		top_3 = srv_ballaz.top_3_ballaz()
		assert top_3[0].get_nume()=="Kobe"
		assert top_3[1].get_nume()=="Curry"
		assert top_3[2].get_nume()=="Bird"
		print("teste business finalizate cu succes")
	