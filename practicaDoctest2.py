import doctest
import math

def raizCuadrada(listaNumeros):
    """
    La función devuelve una lista con la
    raiz cuadrada de los elementos numéricos
    pasados por parámetros en otra lista

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = []
    >>> for i in [9, 16, 25, 36, -49, 64]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """

    return [math.sqrt(n) for n in listaNumeros]

doctest.testmod()

"""
Doctest 2:
    Doctest es un modulo que nos permite hacer hacer varias pruebas a la vez de funciones, clases, etc, que vayamos creando.
    Para esto usaremos el modulo "doctest".

    Los 3 puntos:
        Cuando colocamos 3 puntos quiere decir que esa linea tendra una identacion con respecto a la anterior (como si fuera
        una funcion, un condicional, etc).
        Sintaxis:
            >>> areaCuadrado(lado):
            ...     print("hola")
            ...     return lado*lado
            >>> print(areaCuadrado(4))
        
        Como vemos, usamos los 3 puntos para indicar que estamos identando algo, ademas de estos 3 puntos, tambien debemos
        identar el codigo como si programaramos normalmente.
        Para salir de la identacion simplemente colocamos los signos '>>>' y no hacemos identacion.

        Otra forma de usar los 3 puntos '...' es cuando usamos el doctest, cuando vamos a capturar un error, podemos
        Copiar la PRIMERA Y ULTIMA linea del error y pegarlo en la parte del test de la documentacion, y entre esas 2 lineas
        colocar los 3 puntos '...' identados. Ejemplo:
        
            >>> raizCuadrada(lista)
            Traceback (most recent call last):
                ...
            ValueError: math domain error

        Aqui estamos suponiendo que al llamar a la funcion 'raizCuadrada(lista)' ocurrira un error de tipo 'ValueError'
        y demas informacion, entonces, sabiendo esto, podemos decirle que el resto de la informacion es "comodin", es decir,
        que entre esas 2 lineas de codigo puede ir cualquier linea que se trate del erro, sin importar cuantas sean y sin
        importar lo que nos digan. 
        Esta sería una buena forma para capturar errores en las pruebas con 'doctest'

"""