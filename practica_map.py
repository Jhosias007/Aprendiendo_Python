class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "El empleado {} tiene el cargo de {} y un salario de {}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Presidente", 4000),
    Empleado("Jose", "Viceprecidente", 2000),
    Empleado("Veronica", "Director", 1000),
    Empleado("Lalo", "SubDirector", 750),
    Empleado("Random", "Pro", 75000)
]

def calculoComision(empleado):
    if empleado.salario <= 1000:
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleadosComision = map(calculoComision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)

"""
Funcion Map
    La funcion map nos permite aplicar una funcion a cada elemento de un iterable
    Sintaxis:
        listaEjemplo = map(funcion, iterable)

        "funcion" es la funcion que se aplicara a cada elemento de la lista
        "iterable" es donde se encuentran los elementos a los que se le aplicaran cambios
        En "listaEjemplo" se almacenan los nuevos valores a los que ya se les han aplicado los cambios
"""
