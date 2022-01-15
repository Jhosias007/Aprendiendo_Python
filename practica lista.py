miLista = ["yo", 14, True] * 2
miLista2 = ["hola", "diego"]

sumaLista = miLista + miLista2 #Se pueden sumar listas

miLista.append("Jose")#.append agrega un elemelnto al final de la lista
miLista.insert(1, 90)#agrega un elemento pero te pide un indice para agregar en x porcision de la lista
miLista.extend(["yohohoho"])#.extend es como concatenar la parte final de la lista original con esta linea de codigo

miLista.remove("yo")#.remove elimina un elemento de la lista
miLista.pop()#elimina el ultimo elemento de la lista

print(miLista[:])
print(miLista.index("yo"))#.index busca la posicion en la que se encuentra el valor pedido
print("asd" in miLista)#"in miLista" hace que regrese True o False si el valor pedido esta en la lista

print(sumaLista)


