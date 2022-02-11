import pickle


class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enMarcha,
              "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)


coche1 = Vehiculos("Ferrari",  "M250")
coche2 = Vehiculos("Nissan",  "F800")
coche3 = Vehiculos("Toyota",  "450X")

coches = [coche1, coche2, coche3]

cochesBinario = open("CochesBinario", "wb")

pickle.dump(coches, cochesBinario)

cochesBinario.close()

del (cochesBinario)

obtenerCochesBinario = open("CochesBinario", "rb")

obtenerListaCoches = pickle.load(obtenerCochesBinario)

obtenerCochesBinario.close()

for i in obtenerListaCoches:
    print(i.estado())
