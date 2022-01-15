import pickle

listaNombres = ["Pedro", "Juan", "Ana"]

nombres = open("Lista De Nombres", "wb")

pickle.dump(listaNombres, nombres)

nombres.close()

#del(nombres)

# ------------------------------------------------

nombres = open("Lista De Nombres", "rb")

listaNombres = pickle.load(nombres)

print(listaNombres)


"""
En la primera parte creamos una lista y creamos un archivo con el acceso de esrcitura binaria ("wb")
Luego, con  la funcion pickle.dump pasamos los datos de listaNombres -> nombres y de esta forma convertimos nuestra
Lista en un archivo binario. Al final solo cerramos el archivo y borramos el archivo nombres de lal memoria

En la siguiente parte volvemos a abrir el archivo nombres pero ahora con el modo de acceso de escritura binaria ("rb")
Luego le asignamos a la variable listaNombres lo que nos carge el archivo nombres con la funcion pickle.load(archivo)
Al final solo imprimimos por pantalla lo que se ha almacenado en listaNombres, lo cual ya no será binario, sino sera normal


Con el modo de lectura "wb" le indicamos que vamos a entrar al archivo en forma de edicion binaria
- "w" = write
- "r" = read
- "a" = append

A esto podemos agregarle la letra "b" de binario para saber que estamos tratando con archivos binarios
- "b" = binario

Metodos .dump y .load de pickle:
El metodo pickle.dump() recibe 2 parametros, el primero es el valor de una variable y el otro es el archivo.
Por su traduccion, podemos saber que este metodo hace que el primer parametro ingresado se almacene el en segundo
parametro (siendo este el archivo)

El metodo pickle.load() recibe un parametro, y aquí tiene que ir el nombre de un archivo.
Lo que hace este metodo es cargarnos lo que haiga en un archivo. (Lo podemos almacenar en una variable como en el caso)
"""
