from modulos import funciones_matematicas


class Areas:

    """
    Esta clase captura las areas de
    diferentes figuras geometricas
    """

    def areaCuadrado(lado):
        """
        Calcula el area de el cuadrado
        usando el lado y multiplicandose por si mismo
        """

        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """
        Calcula el area del triangulo
        multiplicando la base por la
        altura entre 2
        """

        return "El area del cuadrado es: " + str((base*altura)/2)


# help(Areas)
help(funciones_matematicas)


# print(areaCuadrado(3))
# print(areaCuadrado.__doc__)
# help(areaCuadrado)

#print(areaTriangulo(3, 5))
# print(areaTriangulo.__doc__)
# help(areaTriangulo)


"""
Documentar Codigo
    Podemos documentar funciones, metodos, clases, modulos, etc. Esto con el fin de saber que funcion cumple lo que estamos 
    haciendo para que alguien mas o nosotros mismos entendamos el codigo mas adelante

    Para documentar funciones, metodos, clases, etc tenemos que colocar comillas triples dentro de la funcion, metodos,
    clases, etc, al inicio de esta. Dentro de estas comillas podemos poner lo que queramos para indicar lo que hace la funcion
    Ejemplo:
        #Funcion:
        def funcionRandom(num1, num2):
            '''
            Documentacion
            Alerta de tanta facha, no mirar
            Ji Ji Ji Ja
            '''

        #Clase:
        class Alumno():
            '''
            Documentacion...
            '''

            #Metodo:
            def __init__(self, *args, **kwargs):
                '''
                Documentacion...
                '''

        #Modulo:
        '''Documentacion'''
        <codigo>
        <codigo><codigo>
        <codigo>


    Para rescatar la documentacion de una funcion hacemos uso del metodo __doc__. Ejemplo:
        print(funcionRandom.__doc__)
    De esta forma nos devolvera la documentacion de la funcion

    Otra forma de rescatar la documentacion es con la funcion help(). Ejemplo:
        help(<funcion>)             - - Devuelve doc. de la funcion
        help(<clase>)               - - Devuelve doc. de la clase y la doc. de sus metodos (si es que hay)
        help(<clase>.<metodo>)      - - Devuelve doc. del metodo
        help(<modulo>)              - - Devuelve doc. del modulo y la doc. de sus funciones (si es que hay)
"""
