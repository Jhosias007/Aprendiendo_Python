class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miMoto = Coche()
desplazamientoVehiculo(miMoto)

"""
1. Creamos una funcion que imprima el parametro que le pasemos (linea 16 - 17)
2. Creamos un objeto (linea 20)
3. Llamamos a la funcion desplazamientoVehiculo y le damos como parametro el nombre del objeto creado (linea 21)

Segun la clase con la que creamos el objeto en la linea 20, se llamara al metodo correspondiete a la clase usada

"""
