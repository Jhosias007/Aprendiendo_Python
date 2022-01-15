from io import open

archivo_texto = open("Archivo.txt", "r+")

archivo_texto.write("Comienzo del texto\n")

#print(archivo_texto.readlines())

listaTexto = archivo_texto.readlines()

listaTexto[1] = "Esta lina ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(listaTexto)

archivo_texto.close()



"""
Podemos crear archivos externos importando la libreria io
Podemos abrir el archivo creado de las siguientes formas: 
- "w" = modificar / escribir
- "r" = leer
- "a"= append / agregar

Los metodos que usamos al llamar a cada una son: (estan en orden)
- "w" = write
- "r" = read / readlines (Con readlines() podemos crear una lista de lo que hay en el archivo)
- "a" = write

Con seek() podemos empezar a leer lo almacenado en el archivo desde la pocision que le demos como parametros. Ej:
ejemplo_texto.seek(5)

Podemos leer la cantidad de caracteres que queramos con el metodo .read() especificandolo en los parametros. Ej:
ejemplo_texto.read(5)

Podemos decirle que accedemos al archivo de forma de lectura y escritura con un "r+"

"""
