import doctest


def areaTriangulo(base, altura):
    """
    Calcula area de triangulo
    >>> areaTriangulo(3, 6)
    'El area es: 9.0'

    >>> areaTriangulo(2, 5)
    'El area es: 5.0'

    >>> areaTriangulo(9, 4)
    'El area es: 18.0'
    """

    return "El area es: " + str((base * altura)/2)


def compruebaMail(mailUsuario):
    """
    Comprueba si el mail ingresado es correcto
    Si no tiene arroba, si tiene mas de una arroba o
    si tiene una arroba al final es incorrecto.
    Por lo contrario, el mail es correcto

    >>> compruebaMail('jhosias@gmail.com')
    True

    >>> compruebaMail('@gmail.com')
    False

    >>> compruebaMail('asdasd.asd@')
    False

    >>> compruebaMail('asd@asd@as.com')
    False
    """

    mail = mailUsuario.count("@")

    if ((mail != 1) or (mailUsuario[-1] == "@") or (mailUsuario.find("@") == 0)):
        return False
    else:
        return True


doctest.testmod()

"""
Doctest
    Doctest es un modulo que nos permite hacer hacer varias pruebas a la vez de funciones, clases, etc, que vayamos creando.
    Para esto usaremos el modulo "doctest".
    Sintaxis:
        import doctest

        def areaCuadrado(lado):
            '''
            Esta funcion permite hallar
            el area de un cuadrado

            >>> areaCuadrado(4)
            16
            
            >>> areaCuadrado(9)
            81
            
            >>> areaCuadrado(5)
            24
            '''

            return int(lado*lado)

        doctest.testmod()

    Como vemos, lo primero que hacemos es importar el modulo "doctest"
    
    Luego creamos una funcion con documentacion, aqui describimos lo que hace la funcion y luego empezamos las pruebas de
    la funcion.
    Lo primero que hacemos es escribir ">>>" estos 3 simbolos como si fueran de la consola de python, luego llamamos a la
    funcion, clase que estemos trabajando y si es necesario le pasamos parametros.
    
    En la siguiente linea, colocamos lo que la funcion nos deberia retornar o devolver, en este caso, los 2 primeros ejemplos
    estan bien pero el ultimo esta mal.

    Si colocamos el valor que retornará la funcion, no ocurrira nada al compilar, de lo contrario, nos dara un error y la
    informacion de que test ha fallado, en este caso, nos dira que en la linea 67 hay un error; nos dirá que le dimos '24'
    pero se esperaba '25'.

    Al final debemos de llamar a la funcion 'testmod()' del modulo 'doctest' como vemos en la linea 73 para que se ejecuten
    estas pruebas que hacemos en la documentacion.

    - Estas pruebas de documentacion nos pueden ayudar cuando hacemos una funcion con varios if-else, o cuando queremos
        ejecutar la funcion con diferentes parametros para ver si funciona correctamente

"""
