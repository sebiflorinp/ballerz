from exceptii.ValidError import ValidError


class ValidatorBaller:
	def valideaza(self, baller):
		erori = ""
		if baller.get_id_baller()<0:
			erori += "id invalid!\n"
		if baller.get_nume() == "":
			erori += "nume invalid!\n"
		if baller.get_valoare()<0.0:
			erori += "valoare invalida!\n"
		if len(erori)>0:
			raise ValidError(erori)