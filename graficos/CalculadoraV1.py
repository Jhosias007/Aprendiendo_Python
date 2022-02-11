from tkinter import *

raiz = Tk()
frame = Frame(raiz)
frame.pack()

raiz.resizable(False, False)

# ---------- Variables ----------

resultado = 0
operacion = ""
num1 = 0
num2 = 0
resetearPantalla = False

# ---------- Pantalla de numeros ----------


numeroPantalla = StringVar()

pantalla = Entry(frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, columnspan=6)
pantalla.config(bg="gray", fg="black", border=4,
                relief="groove", justify="right")

# ---------- Funciones ----------


def mostrarNumero(num):
    global operacion
    global resetearPantalla
    global num1
    global num2

    if resetearPantalla == True:
        # Con esta linea conseguimos reiniciar el valor de la pantalla
        numeroPantalla.set(num)
        resetearPantalla = False

    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def sumar(num):
    global resultado
    global operacion
    global num1
    global resetearPantalla

    operacion = "suma"
    resultado += float(num)
    resetearPantalla = True
    numeroPantalla.set(resultado)


contadorResta = 0


def restar(num):
    global resultado
    global operacion
    global num1
    global resetearPantalla
    global contadorResta

    if contadorResta == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contadorResta == 1:
            resultado = num1 - float(num)
        else:
            resultado = resultado - float(num)

    contadorResta += 1
    numeroPantalla.set(resultado)
    operacion = "resta"
    resetearPantalla = True


contadorMult = 0


def multiplicar(num):
    global operacion
    global resultado
    global num1
    global resetearPantalla
    global contadorMult

    if contadorMult == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contadorMult == 1:
            resultado = num1 * float(num)
        else:
            resultado = resultado * float(num)

    resetearPantalla = True
    numeroPantalla.set(resultado)
    contadorMult += 1
    operacion = "multiplicacion"


contadorDiv = 0


def dividir(num):
    global resultado
    global operacion
    global num1
    global resetearPantalla
    global contadorDiv

    if contadorDiv == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contadorDiv == 1:
            resultado = num1 / float(num)
        else:
            resultado = resultado / float(num)

    resetearPantalla = True
    numeroPantalla.set(resultado)
    operacion = "division"
    contadorDiv += 1


def accionBotonC():
    global num1
    global resetearPantalla
    global resultado
    global contadorResta, contadorDiv, contadorMult
    global operacion

    numeroPantalla.set("")
    #num1 = 0
    resultado = 0
    operacion = ""
    contadorMult = 0
    contadorResta = 0
    contadorDiv = 0


def accionBotonCE():
    global numeroPantalla

    numeroPantalla.set("")


def accionBotonDel():
    global numeroPantalla

    # Obtengo la lista de caracteres que hay en pantalla
    listaNumeroPantalla = list(numeroPantalla.get())
    listaNumeroPantalla.pop()  # Borro el ultimo valor almacenado en la cadena creada arriba
    # Vuelvo la lista en un str con el metodo .join()
    listaNumeroPantalla = "".join(listaNumeroPantalla)
    numeroPantalla.set(listaNumeroPantalla)


def accionBotonResultado():
    global resultado
    global operacion
    global num1
    global contadorResta
    global contadorMult
    global contadorDiv
    global contadorResultado

    if operacion == "suma":
        numeroPantalla.set(resultado + float(numeroPantalla.get()))
        resultado = 0

    elif operacion == "resta":
        numeroPantalla.set(resultado - float(numeroPantalla.get()))
        resultado = 0
        contadorResta = 0

    elif operacion == "multiplicacion":
        numeroPantalla.set(resultado * float(numeroPantalla.get()))
        resultado = 0
        contadorMult = 0

    elif operacion == "division":
        numeroPantalla.set(resultado / float(numeroPantalla.get()))
        resultado = 0
        contadorDiv = 0

# ---------- Botones ----------


botonCE = Button(frame, text="CE", width=4, command=lambda: accionBotonCE())
botonCE.grid(row=2, column=1, padx=2, pady=2)

botonC = Button(frame, text="C", width=4,
                command=lambda: accionBotonC())
botonC.grid(row=2, column=2, padx=2, pady=2)

botonEliminar = Button(frame, text="DEL", width=4,
                       command=lambda: accionBotonDel())
botonEliminar.grid(row=2, column=3, padx=2, pady=2)

botonDividir = Button(frame, text="/", width=4,
                      command=lambda: dividir(numeroPantalla.get()))
botonDividir.grid(row=2, column=4, padx=2, pady=2)


#

boton1 = Button(frame, text="1", width=4,
                command=lambda: mostrarNumero("1"), bg="#C8C8C8")
boton1.grid(row=5, column=1, padx=2, pady=2)

boton2 = Button(frame, text="2", width=4,
                command=lambda: mostrarNumero("2"), bg="#C8C8C8")
boton2.grid(row=5, column=2, padx=2, pady=2)

boton3 = Button(frame, text="3", width=4,
                command=lambda: mostrarNumero("3"), bg="#C8C8C8")
boton3.grid(row=5, column=3, padx=2, pady=2)

botonSuma = Button(frame, text="+", width=4,
                   command=lambda: sumar(numeroPantalla.get()))
botonSuma.grid(row=5, column=4, padx=2, pady=2)

#

boton4 = Button(frame, text="4", width=4,
                command=lambda: mostrarNumero("4"), bg="#C8C8C8")
boton4.grid(row=4, column=1, padx=2, pady=2)

boton5 = Button(frame, text="5", width=4,
                command=lambda: mostrarNumero("5"), bg="#C8C8C8")
boton5.grid(row=4, column=2, padx=2, pady=2)

boton6 = Button(frame, text="6", width=4,
                command=lambda: mostrarNumero("6"), bg="#C8C8C8")
boton6.grid(row=4, column=3, padx=2, pady=2)

botonResta = Button(frame, text="-", width=4,
                    command=lambda: restar(numeroPantalla.get()))
botonResta.grid(row=4, column=4, padx=2, pady=2)

#

boton7 = Button(frame, text="7", width=4,
                command=lambda: mostrarNumero("7"), bg="#C8C8C8")
boton7.grid(row=3, column=1, padx=2, pady=2)

boton8 = Button(frame, text="8", width=4,
                command=lambda: mostrarNumero("8"), bg="#C8C8C8")
boton8.grid(row=3, column=2, padx=2, pady=2)

boton9 = Button(frame, text="9", width=4,
                command=lambda: mostrarNumero("9"), bg="#C8C8C8")
boton9.grid(row=3, column=3, padx=2, pady=2)

botonMult = Button(frame, text="x", width=4,
                   command=lambda: multiplicar(numeroPantalla.get()))
botonMult.grid(row=3, column=4, padx=2, pady=2)

#

boton0 = Button(frame, text="0", width=4,
                command=lambda: mostrarNumero("0"), bg="#C8C8C8")
boton0.grid(row=6, column=2, padx=2, pady=2)

botonPunto = Button(frame, text=",", width=4,
                    command=lambda: mostrarNumero("."))
botonPunto.grid(row=6, column=1, padx=2, pady=2)

botonIgual = Button(frame, text="=", width=10,
                    command=lambda: accionBotonResultado())
botonIgual.grid(row=6, column=3, padx=2, pady=2, columnspan=2)

raiz.mainloop()
