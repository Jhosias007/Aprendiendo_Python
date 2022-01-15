import pickle

class Persona():
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona con el nombre " + self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas():

	personas = []

	def __init__(self):
		listaDePersonas = open("Lista De Personas", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas = pickle.load(listaDePersonas)
			print("Se han cargado {} personas del fichero externo".format(len(self.personas)))
		except:
			print("No se han cargado personas")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)


	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFichero()

	def mostrarPersonas(self):
		for i in self.personas:
			print(i)

	def guardarPersonasEnFichero(self):
		listaDePersonas = open("Lista De Personas", "wb")
		pickle.dump(self.personas, listaDePersonas)

	def mostrarInformacionFichero(self):
		print("Informacion del fichero externo: ")
		for i in self.personas:
			print(i)

miListaPersonas = ListaPersonas()
persona = Persona("Jose", "Masculino", 24)
miListaPersonas.agregarPersonas(persona)
miListaPersonas.mostrarInformacionFichero()

# Ten cuidado al usar el self
