import math

def calcularRaiz(n1):
    if n1 < 1:
        raise ValueError("El numero no puede ser negativo")

    else:
        return math.sqrt(n1)



insertarNumero = int(input("Numero: "))

try:

    print(calcularRaiz(insertarNumero))

except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")

"""
- Con raise podemos crear nuestro propio error. 
- Podemos darle un subnombre o otro nombre a el error a la hora de poner el bloque except
"""