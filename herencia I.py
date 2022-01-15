class Vehiculos():
    def __init__(self, marca, modelo) -> None:
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


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.carga = 100
    
    def cargarEnergia(self):
        self.cargando = True

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado == True:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos): #Al poner una clase como parametro de otra clase, estamos heredando lo que tiene esta clase padre
    hacerCaballito = ""
    def caballito(self):
        self.hacerCaballito = "Voy haciendo caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enMarcha, 
        "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n", self.hacerCaballito)

moto1 = Moto("Honda", "CBR")
moto1.caballito()
moto1.estado()

print()

furgoneta1 = Furgoneta("Renault", "Kangoo")
furgoneta1.arrancar()
furgoneta1.estado()
print(furgoneta1.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

bici1 = BicicletaElectrica("ToyoTa", "c13")


