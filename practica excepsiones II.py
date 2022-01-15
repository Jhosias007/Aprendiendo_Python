def dividir():
    try:    
        n1 = float(input("Numero 1 :"))
        n2 = float(input("Numero 2 :"))

        print("El resultado de la division es: " + str(n1 / n2))
        print("Programa concluido")

    except: # De esta forma podemos capturar todos los errores que se generen al correr el programa
            # y hacer que el programa fluya, aunque no se recomienda ya que no se especifica el error al usuario
        print("Ha ocurrido un error")

def dividir2():
    try:    
        n1 = float(input("Numero 1 :"))
        n2 = float(input("Numero 2 :"))

        print("El resultado de la division es: " + str(n1 / n2))
        print("Programa concluido")

    except ValueError:
        print("Debes ingresar un numero!")

    except ZeroDivisionError:
        print("No puedes dividir entre cero!")

def dividir3():
    try:    
        n1 = float(input("Numero 1 :"))
        n2 = float(input("Numero 2 :"))

        print("El resultado de la division es: " + str(n1 / n2))
    
    finally: #con finally podemos hacer que pase lo que pase, se ejecute lo que este dentro del bloque

        print("Programa concluido")

    

dividir()
print()
dividir2()

"""
- El try funciona de una forma similar a un condicional (if):
    cuando ponemos un bloque de "try" estamos haciendo que la computadora intente hacer lo que le pedimos,
    en otro caso, realizara otra accion que le diremos en el bloque "except".
- Podemos anidar varios "except" a un solo "try".
- Podemos poner el bloque except sin ninguna especificacion de error para no escribir cada situacion de error
    pero no se recomienda ya que al realizarlo no podremos especificar al usuario sobre cual a sido su error.
- Podemos usar el finally como otra forma de termir el try, este nos permitira saltarnos todos los errores
y continuar con el programa pero al final botara el error
- El finally se usa para hacer que algo suceda si o si, en caso de que hayan errores de ejecucion del programa
"""