class Coche():

    def __init__(self):  # Creando una funcion con el nombre __init__ y el parametro self, estamos indicando
        # que ese será el estado inicial al crear un objeto de esa clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancar):
        self.__enMarcha = arrancar  # el self hace referencia hacia el mismo objeto

        if self.__enMarcha == True:
            chequeo = self.__chequeoInterno()

        if self.__enMarcha == True and chequeo == True:
            return "El coche esta en marcha"

        elif self.__enMarcha == True and chequeo == False:
            return "Algo ha fallado en el chequeo, no podemos arrancar"

        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de", self.__anchoChasis, "y un largo de",
              self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()  # Esto se denomina como: instanciar una clase
print(miCoche.arrancar(True))
miCoche.estado()

print()

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.estado()



"""
El self es completamente necesario como atributo en un metodo
- El self representa al mismo objeto, por ejemplo, creamos un objeto llamado MiCoche, entonces,
    self lo que hace es tomar el valor de MiCoche

Para crear un objeto primero ponemos un nombre como a una variable y le decimos que es igual a la clase 
    que le queremos asignar

"""
