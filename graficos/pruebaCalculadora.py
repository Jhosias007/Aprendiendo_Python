from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""
num1 = IntVar()
num2 = IntVar()

#Pantalla -----------------------------------------------------------------

agregaNumero = StringVar()

pantalla = Entry(miFrame, textvariable = agregaNumero, numvariable = num1 and num2)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(background = "black", fg = "#03f943", justify = "right")

#Agregar numero

def mostrarNum(num):
	agregaNumero.set(pantalla.get() + num)

#Funcion sumar:

def accionSumar():
	resultado = num1 + num2
	return resultado

#Botones Fila 1 -----------------------------------------------------------

boton7 = Button(miFrame, text = "7", width = 3, command = lambda: mostrarNum("7"))
boton7.grid(row = 2, column = 1)

boton8 = Button(miFrame, text = "8", width = 3, command = lambda: mostrarNum("8"))
boton8.grid(row = 2, column = 2)

boton9 = Button(miFrame, text = "9", width = 3, command = lambda: mostrarNum("9"))
boton9.grid(row = 2, column = 3)

botonDiv = Button(miFrame, text = "/", width = 3)
botonDiv.grid(row = 2, column = 4)

#Botones Fila 2 -----------------------------------------------------------

boton4 = Button(miFrame, text = "4", width = 3, command = lambda: mostrarNum("4"))
boton4.grid(row = 3, column = 1)

boton5 = Button(miFrame, text = "5", width = 3, command = lambda: mostrarNum("5"))
boton5.grid(row = 3, column = 2)

boton6 = Button(miFrame, text = "6", width = 3, command = lambda: mostrarNum("6"))
boton6.grid(row = 3, column = 3)

botonMult = Button(miFrame, text = "*", width = 3)
botonMult.grid(row = 3, column = 4)

#Botones Fila 3 -----------------------------------------------------------

boton1 = Button(miFrame, text = "1", width = 3, command = lambda: mostrarNum("1"))
boton1.grid(row = 4, column = 1)

boton2 = Button(miFrame, text = "2", width = 3, command = lambda: mostrarNum("2"))
boton2.grid(row = 4, column = 2)

boton3 = Button(miFrame, text = "3", width = 3, command = lambda: mostrarNum("3"))
boton3.grid(row = 4, column = 3)

botonRest = Button(miFrame, text = "-", width = 3)
botonRest.grid(row = 4, column = 4)

#Botones Fila 4 -----------------------------------------------------------

botonComa = Button(miFrame, text = ",", width = 3, command = lambda: mostrarNum(","))
botonComa.grid(row = 5, column = 1)

boton0 = Button(miFrame, text = "0", width = 3, command = lambda: mostrarNum("0"))
boton0.grid(row = 5, column = 2)

botonSuma = Button(miFrame, text = "+", width = 3)
botonSuma.grid(row = 5, column = 3)

botonIgual = Button(miFrame, text = "=", width = 3)
botonIgual.grid(row = 5, column = 4, columnspan = 4)



raiz.mainloop()


"""
Extras:

Metodos:

Parametros:
	- columnspan = x = Lo que hace es usar la cantidad de columnas que le indiquemos
	- rowspan = x = Lo que hace es usar la cantidad de filasque le indiquemos

"""