import re

cadena = "Vamos a aprender exexpresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar = "Python"

print(len(re.findall(textoBuscar, cadena)))

"""
if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

tetxoEncontrado = re.search(textoBuscar, cadena) # Con el metodo re.search() le decimos que busce un texto en una cadena

print(tetxoEncontrado.start())  # Encuentra el inicio del texto encontrado
print(tetxoEncontrado.end())    # Encuentra el filan del texto encontrado
print(tetxoEncontrado.span())   # Encuentra el inicio y final del texto encontrado
"""

"""
Expresiones regulares
    re.search(cadenaEspecifica, cadenaGrande)
    Busca la cadena especifica en la cadena grande. Devuelve un obcect si lo encuentra, si no, devuelve None

    re.findall(cadenaEspecifica, cadenaGrande)
    Devuelve una lista de las todas las palabras que coninsiden con la cadenaGrande
    Con len() podemos obtener el valor repetido en numeros

    .start() 
    Devuelve el inicio de donde se encontro la cadena en la cadenaGrande
    El metodo debe aplicarse a una variable re.search()

    .end()
    Devuelve el final de donde se encontro la cadena en la cadenaGrande
    El metodo debe aplicarse a una variable re.search()
    
    .span()
    Devuelve el inicio y final en una lista de donde se encontro la cadena en la cadenaGrande
    El metodo debe aplicarse a una variable re.search()

"""

# C: 111 - P: 1
