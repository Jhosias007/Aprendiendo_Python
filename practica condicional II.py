print("Control del salario en la escuela")

salarioDirector = int(input("Salario del Director: "))
print("El salaraio del director es de " + str(salarioDirector) + " soles")

salarioSubDirector = int(input("Salario del Sub Director: "))
print("El salaraio del Sub Director es de " + str(salarioSubDirector) + " soles")

salarioMaestro= int(input("Salario del Maestro: "))
print("El salaraio del Maestro es de " + str(salarioMaestro) + " soles")

if salarioMaestro < salarioSubDirector < salarioDirector:
	print("La escuela funciona correctamente")

else:
	print("Algo anda mal en la escuela")


