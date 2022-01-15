email = input("Escribe tu email: ")

for i in email:

    if i == "@":
        arroba = True
        break;

else: # Podemos poner un else acompañado de un bucle (for ó while) aunque no puede ser muy efectivo en todos los casos   
    arroba = False

print(arroba)
