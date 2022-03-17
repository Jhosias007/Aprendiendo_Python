import re

"""
cadena = "Vamos a aprender exexpresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar = "Python"

print(len(re.findall(textoBuscar, cadena)))


if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

tetxoEncontrado = re.search(textoBuscar, cadena) # Con el metodo re.search() le decimos que busce un texto en una cadena

print(tetxoEncontrado.start())  # Encuentra el inicio del texto encontrado
print(tetxoEncontrado.end())    # Encuentra el filan del texto encontrado
print(tetxoEncontrado.span())   # Encuentra el inicio y final del texto encontrado
"""

contador = 1

lista_nombres = ["Ana Gómez",
    "Maria Martin",
    "Sandra López",
    "Santiago Martin",
    "Sandra Ferndandez",
    "Pedro",
    "Jose",
    "Anita",
    "Gonter"
]

lista_links = [
    "https://youtube.com",
    "https://twetter.com",
    "https://gmail.com",
    "https://gmail.es",
    "https://outlook.es"
]

lista_links = [
    "https://youtube.com",
    "https://twetter.com",
    "https://gmail.com",
    "https://gmail.es",
    "https://outlook.es"
]

lista_BuscadorEspesifico= [
    "http://informaticaemespaña.es",
    "http://pildorasinformaticas.es",
    "http://pildorasinformaticas.com"
]

lista_BuscadorEspesifico2= [
    "hombres",
    "mujeres",
    "niños",
    "niñas"
]

lista_BuscadorEspesifico3= [
    "hombres",
    "mujeres",
    "camion",
    "camión"
]

lista_Estados = [ 
    "Ma1",
    "Se1",
    "Ma2",
    "Bal",
    "Ma3",
    "Val",
    "Va2",
    "Ma4",
    "Ma:A",
    "Ma.5",
    "MaB",
    "Ma:c"
]

#for elemento in lista_links:
#    if re.findall(".es$", elemento):
#        print(".es", elemento)

#for elemento in lista_BuscadorEspesifico:
#    if re.findall("niñ[oa]s", elemento):
#        print(elemento)

#for elemento in lista_BuscadorEspesifico3:
#    if re.findall("cami[oó]n", elemento):
#        print(elemento)

#for elemento in lista_nombres:
#    if re.findall("[o-t]$", elemento): # [o-t] <- De esta forma buscamos rangos (pueden ser entre letras o numeros)
#        print(contador, elemento)
#        contador += 1

for elemento in lista_Estados:
    #if re.findall("Ma[0-3A-B]", elemento):
    if re.findall("Ma[.:]", elemento):
        print(contador, elemento)
        contador += 1

#Documentacion
"""
Expresiones regulares
    re.search(cadenaEspecifica, cadenaGrande)
    Busca la cadena especifica en la cadena grande. Devuelve un obcect si lo encuentra, si no, devuelve None

    re.findall(cadenaEspecifica, cadenaGrande)
    Devuelve una lista de las todas las palabras que coninsiden con la cadenaGrande
        - Con len() podemos obtener el valor repetido en numeros

        - Colocando distintos caracteres entre corchetes en "cadenaEspecifica" podremos lograr que nos den
            todas las palabras que contengan los valores ingresados en los corchetes. Ejemplo:
            Si le ponemos esto ("[oó]", cadenaGrande) nos devolvera todas las palabras con la letra o y 
                las palabras con la letra ó (con tilde)
            Podemos hacer algo similar de la siguiente palabra: ("cami[oó]n", cadenaGrande), de este modo
                nos devolvera todas las palabras "camion" con y sin tilde.
    
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


