"""
nombre = input("Introduce tu nombre de usuario ")
print("El nombre de usuario es: " + nombre.capitalize())
"""

edad = input("Introduce tu edad: ")

while edad.isdigit() == False:
    print("Introduce un numero")
    edad = input("Edad: ")
    
edad = int(edad)

if edad < 18:
    print("No puedes pasar")
else:
    print("Puedes pasar")


