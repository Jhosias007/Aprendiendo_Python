from cgitb import text
from distutils import command
from tkinter import *

root = Tk()
root.title("Check Button")

frame = Frame(root, width=20)
frame.pack()

playa = IntVar()
montaña = IntVar()
turismoRural = IntVar()


def opcionesViaje():

    opcionEscogida = ""

    if playa.get() == 1:
        opcionEscogida += " Playa"

    if montaña.get() == 1:
        opcionEscogida += " Montaña"

    if turismoRural.get() == 1:
        opcionEscogida += " Turismo Rural"

    textoFinal.config(text=opcionEscogida)


texto = Label(frame, text="Selecciona tu destino").pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1,
            offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1,
            offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural,
            onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
# 12
