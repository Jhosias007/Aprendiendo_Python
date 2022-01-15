def evaluaEdad(edad):
    if edad<0:
      raise TypeError("JOTARO, que tonto")  
    elif edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres mayor"
    elif edad < 100:
        return "Cuidate"

print(evaluaEdad(-3))


"""
raise es una forma de lanzar un error de ejecucion. Las utilidades para esto son pocas
"""