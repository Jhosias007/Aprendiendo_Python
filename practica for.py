"""for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
	print(i)
"""



"""
for i in "Juanito":
	print("Hola", end = " ")
"""



"""
email = False

for i in "juanito_perez@gmail.com":
	if (i == "@"):
		email = True

if email:	#Podemos hacer un condicional de una variable booleana sin poner que es igual a True,
			#Ya que es su valor default
	print("El email es correcto")
else:
	print("El email es incorrecto")
"""


"""
contadorEmail = 0
emailUsuario = input("Introduce tu email: ")

for i in emailUsuario:
	if (i == "@") or (i == "."):
		contadorEmail = contadorEmail + 1

if contadorEmail == 2:
	print("El email es correcto")
else:
	print("El email es incorrecto")
"""



"""
for i in range(5): #range crea la cantidad de valores que le pases como parametros
	print(i)
"""


"""
for i in range(20, 42, 2):	#range puede recibir 3 parametros de numeros. El primero es donde inicia el contador
							#el segundo indica hasta donde llega el contador y el ultimo indica de cuanto en cuanto va a contar
							#si solo tiene un parametro quiere decir que hará un conteo desde el 0 hasta el numero indicado menos 1
							#si solo hay dos hará un conteo entre esos dos numeros
	print(f"valor del 20 al 40 de 2 en 2: {i}")
"""


validacionEmail = False
email = input("Escribe tu email: ")

for i in range(len(email)):
	if email[i] == "@":
		validacionEmail == True

if validacionEmail == True:
	print("Email correcto")
else:
	print("Email incorrecto")

#no me funciona esto nose pq

