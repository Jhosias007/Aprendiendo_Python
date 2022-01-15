"""
print("ASIGNATURAS AÑO 2029")
print("Asignaturas optativas: INFORMATICA GRAFICA - PRUEBAS DE SOFTWARE - USABILIDAD Y ACCESIBILIDAD")
asignaturaElegida = input("Escribe la asiguatura que quieras: ").lower()

asignaturasSobrantes = ["informatica grafica", "pruebas de software", "usabilidad y accesibilidad"]

if asignaturaElegida in (asignaturasSobrantes):
	print("Asignatura elegida: " + asignaturaElegida)
else:
	print("La asignatura no se encuentra disponible")
"""

nombre = "Jhosias Andre"
contador = 0

for i in nombre:

	if i == " ":
		continue

	contador+=1


print(contador)


