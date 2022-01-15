print("verificacion de gmail del usuario".upper())
gmail = input("Ingresa tu gmail: ")

while True:

    while gmail.count("@") >= 2:
        print("Solo debes ingresar una arroba")
        gmail = input("Ingresa tu gmail: ")

    while gmail.count("@") <= 0:
        print("Debes colocar una arroba!")
        gmail = input("Ingresa tu gmail: ")

    while gmail.startswith("@") == True:
        print("No debes comenzar con arrobas")
        gmail = input("Ingresa tu gmail: ")

    while gmail.endswith("@") == True:
        print("No puedes poner un arroba al final")
        gmail = input("Ingresa tu gmail: ")
    """
        while gmail.endswith(".com") == False or gmail.endswith(".es") == False:
            print("Tienes que colocar .com ó .es al final")
            gmail = input("Ingresa tu gmail: ")
    """
    if gmail.count("@") == 1 and gmail.startswith("@") == False and gmail.endswith("@") == False:
        print("El gmail ingresado es correcto")
        break;


# while infinito con break al poner gmail correcto
