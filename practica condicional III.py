print("PROGRAMA DE BECAS")
print("")

distanciaEscuela = int(input("Distancia a la escuela de tu casa en kilometros: "))

numeroHermanos = int(input("Numero de hermanos: "))

salarioFamiliar = int(input("Salario Familiar: "))

print("")

print("Tus datos son:")
print("Distancia de la escuela a tu casa: "  + str(distanciaEscuela) + " km")
print("Numero de hermanos: " + str(numeroHermanos) + " hermanos")
print("El salario familiar: " + str(salarioFamiliar) + " soles mensuales")
print("")

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 1000:
	print("Lo que indica que SI tienes derecho a una beca")
else:
	print("Lo que indica que NO tienes derecho a una beca")


