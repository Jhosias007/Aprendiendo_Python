def funcionDecoradora(funcionParametro):
    def funcionInterna(*args, **kwargs):
        print("Estamos realizando un calculo")
        funcionParametro(*args, **kwargs)
        print("Hemos terminado el calculo")
        print()
    return funcionInterna

@funcionDecoradora
def suma(num1: int, num2: int, num3:int):
    print("Suma: ", num1 + num2 + num3)

@funcionDecoradora
def resta(num1: int, num2: int):
    print("Resta: ", num1 - num2)

@funcionDecoradora
def potencia(base: int, exponente: int):
    print(pow(base, exponente))

suma(7, 5, 8)
resta(12, 10)
potencia(exponente=3, base=5)

"""
Funciones Decoradoras
    Las funciones decoradoras son funciones que agregan mas codigo a una funcion
    Sintaxis:
        def funcionDecoradora(funcionAEditar):
            def funcionInterior():
                <codigo>
                <codigo>
                
                funcionAEditar()
                
                <codigo>
                <codigo>
            
            return funcionInterior

    Primero definimos una funcion y le decimos que recibira un parametro (este parametro es la funcion que se "decorara")
    
    Dentro de la funcion principal creamos una funcion interior que es en donde estara el codigo que queremos 
    agregar a otras funciones. A partir de aqui podremos poner todo el codigo que queramos pero en algun punto debemos
    llamar al parametro de la funcion principal como si fuera una funcion. Ej: funcionAEditar()
    Esto es para que en algun punto se llame a la funcion, sino nunca se agregara el codigo adicional

    Al final, regresamos la identacion a la funcion principal y retornamos la funcion interior

    Para que el programa sepa que funciones seran decoradas, antes de declarar la funcion a decorar, debemos poner algo asi:
        @funcionDecoradora          <---- Si, sin parentesis
    Con esto le indicamos que la siguiente funcion debe ser decorada

*args
    *args se utiliza para indicar que una funcion que estamos creando recibira un numero indeterminado de parametros
    Ejemplo: funcion(12, 123, 83, 8774)

**kwargs
    **kwargs se usa para indicar que se recibira un numero indeterminado de parametros con clave valor.
    Ejemplo: funcion(num1=12, num2=123, num3=83, num4=8774)
    


"""