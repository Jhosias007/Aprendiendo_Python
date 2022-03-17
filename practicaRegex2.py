import re

nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"
nombre4 = "1asd"

codigo1 = "kjfdklasdfjkfsdafjs71dskñfñjñsa"
codigo2 = "lkd<sfjas71kslafjasdñafjñlasñdfsdjfsñdfjsdlñ"
codigo3 = "slkdjslañfdjfslñdjfsdl"

#if re.match(".ara", nombre1, re.IGNORECASE):
#    print("Hemos encontrado el nombre")
#else:
#    print("No lo hemos encontrado el nombre")

#if re.match("\d", nombre4, re.IGNORECASE):
#    print("Hemos encontrado el nombre")
#else:
#    print("No lo hemos encontrado el nombre")

if re.search("71", codigo3, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado el nombre")
#https://www.youtube.com/watch?v=DQXm6bIZgvk&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=74
# C: 121 - P: 1
"""
Expresiones Regulares:
    re.match(cadenaEspecifica, cadenaGrande, re.IGNORECASE)
    Sirve para buscar una cadena especifica en el INICIO otra cadena grande, el tercer parametro es 
    para ignorar muyusculas y minusculas y solo buscar los caracteres
        - Podemos hacer uso de "." en vez de un caracter especifico (equivale masomenos a cualquier caracter)
        - Podemos saber si una "cadenaGrande" empieza por un numero si usamos "\d" como "cadenaEspecifica"

    re.search(cadenaEspecifica, cadenaGrande, re.IGNORECASE)
    Sirve para buscar una cadena especifica en CUALQUIER PARTE de "cadenaGrande", el tercer parametro es 
    para ignorar muyusculas y minusculas y solo buscar los caracteres



    re.search(cadenaEspecifica, cadenaGrande, re.IGNORECASE)
"""
