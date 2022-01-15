#las tuplas no se pueden modificar luego de declararse

miTupla = ("Juan", ) #tupla unitaria
print(len(miTupla)) #len es la cantidad

miTupla2 = "Juanito" #tupla sin parentesis, no se recomienda evitar los parentesis por confusion
#print(miTupla2)

miTupla3 = ("Pedro", 1, 10, 2021)
nombre, dia, mes, año = miTupla3

print(nombre)	#Esto es el desempaquetado de tupla
print(dia)		#Esto es el desempaquetado de tupla
print(mes)		#Esto es el desempaquetado de tupla
print(año)		#Esto es el desempaquetado de tupla


#las tuplas pueden convertirse a lista y vicebersa
#no se pueden aplicar .index