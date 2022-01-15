print("Estado de notas")

nota = int(input("Nota: "))

if nota < 0:
	print("Nota incorrecta")

elif nota < 10:
	print("Insuficiente")

elif nota < 13:
	print("Suficiente")

elif nota < 16:
	print("Nota correcta")

elif nota < 18:
	print("Logrado")

elif nota <= 20:
	print("Destacado")

else:
	print("La nota ingresada esta fuera del rango")
