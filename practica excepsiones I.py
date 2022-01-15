#las excepciones se dan al correr el programa, es un error no esperado, por ejemplo, 
#cuando el usuario ingresa valores de tipo str cuando deverian ser int u otros
#podemos capturar estos errores y seguir con el resto del programa con el uso de "try" y "except"

def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No puedes dividir entre 0, jijijija")
        return("Error de division")

while True:
    try:
        n1 = int(input("Numero 1: "))
        break;

    except ValueError:
        print("Debes colocar un numero nada mas, intentalo de nuevo")

while True:
    try:
        n2 = int(input("Numero 2: "))
        break;

    except ValueError:
        print("Debes colocar un numero nada mas, intentalo de nuevo")


print("Elige tu operacion: ")
print("Suma - s")
print("Resta - r")
print("Multiplicacion - m")
print("Division - d")
operacion = input()
operacion = operacion.lower()

if operacion == "s":
    print("El resultado es :", sumar(n1, n2))

elif operacion == "r":
    print("El resultado es :", restar(n1, n2))

elif operacion == "m":
    print("El resultado es :", multiplicar(n1, n2))

elif operacion == "d":
    print("El resultado es :", dividir(n1, n2))

else:
    print("Operacion no valida")

print("Continuacion del programa...")

