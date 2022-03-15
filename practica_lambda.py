# Funcion Normal
def areaTriangulo(base: int, altura: int):
    return (base * altura) / 2

print(areaTriangulo(5, 4))

# Funcion Lambda
areaTriangulo2 = lambda base, altura: (base * altura) / 2

print(areaTriangulo2(3, 5))

"""
Funciones Lambda:
    Las funciones lambda son funciones de una sola linea que se usan para realizar tarias muy simples
    Sintaxis:
        nombre_FuncionLambda = lambda parametroNum1, parametroNum2 : (parametroNum1 * parametroNum2) / 2
        
        Nota: La parte que continua de los dos puntos es lo que se va a retornar
"""