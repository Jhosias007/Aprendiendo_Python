"""def generarPares(limite):
    num = 1
    lista1 = []

    while num < limite:
        lista1.append(num*2)
        num = num + 1
    
    return lista1

print(generarPares(10))
"""

def generarPares2(limite):
    num = 1

    while num < limite:
        yield num * 2
        num = num + 1
    
obtenerPares2 = generarPares2(10)


print(next(obtenerPares2)) # la funcion de next hace que imprima el siguiente valor de el generador (objeto iterable)

print("Spam")

print(next(obtenerPares2)) # la funcion de next hace que imprima el siguiente valor de el generador (objeto iterable)

print("Spam")

print(next(obtenerPares2)) # la funcion de next hace que imprima el siguiente valor de el generador (objeto iterable)

print("Spam")


