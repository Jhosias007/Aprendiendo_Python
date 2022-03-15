"""lista = [12, 15, 124, 92, 57]

# Forma con funcion normal
def numeroPar(num):
    if num % 2 == 0:
        return True


print(list(filter(numeroPar, lista)))

# Forma con funcion lambda

print(list(filter(lambda num: num % 2 == 0, lista)))
"""

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

salariosAltos = filter(
    lambda empleado: empleado.salario > 3000, listaEmpleados)

for i in salariosAltos:
    print(i)

"""
Funcion Filter
    La funcio filter se usa para crear un iterador que dentro de ella haigan elementos que cumplan una condicion indicada
    Sintaxis:
        lista = filter(funcion, iterador)
    
        En "lista" estamos guardando los elementos del "iterador" que hayan cumplido una condicion que se encuentre en la
        "funcion"
        "lista" es de tipo objeto, por lo que si queremos ver lo que ha almacenado, podemos hacerlo convirtiendolo en una lista

"""
