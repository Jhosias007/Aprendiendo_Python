"""
i = 1

while i <= 10:
	print("Ejecucion numero " + str(i))
	i = i + 1

print("Fin de el programa")
"""


"""
edad = int(input("Introduce tu edad: "))

while edad <= 4 or edad > 100:
	edad = int(input("Tu edad es incorrecta, vuelve a digitarla por favor: "))

print("Grasa por colaborar mano.")
"""

import math

print("Elevacion cuadrada de un numero")
numero = int(input("Escribe  un numero: "))

intentos = 0

while numero < 0:
	print("No se puede elevar un numero negativo")
	numero = int(input("Escribe  un numero: "))
	intentos = intentos + 1

	if intentos == 2:
		print("Has perdido tus intentos. El programa a finalizado")
		break

if intentos < 2:
	resultado = math.sqrt(numero)
	print("El resultado es: " + str(resultado))


