def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "desaprobado"
	return valoracion

print("Valoracion de notas de alumnos")
ingresarNota = int(input("Nota: "))

print(evaluacion(ingresarNota))
