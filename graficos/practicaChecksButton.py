from tkinter import *

root = Tk()
root.title("Check Button")

frame = Frame(root)
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

textoFinal = Label(frame, width=35)
textoFinal.pack()


root.mainloop()
# 20


"""
Checkbutton:
    Similar al Radiobuttom, pero los Checkbutton se utilizan para hacer una seleccion multiple
    Sintaxis:
        ejemploCheckbutton = Checkbutton(root, text="Buenos Dias", variable=var2,
                                            onvalue=True, offvalue, command=ejecutar, *)

    Podemos obtener su valor relacionando el Checkbutton a una variable y con otros parametros como
    onvalue=True, offValue=False; (podemos poner cualquier tipo de variable, solo es un ejemplo).
    De este modo y asociando el Checkbutton a una funcion podremos obtener cuales de las casillas estan
    seleccionadas.
    
    Lo que haiga en value se almacena en la variable pasada por parametros

Parametros:
    value:
        Se utiliza para asignar un valor cuando el objeto este seleccionado, por ejemplo, podemos poner esto:
            value=1; value="a";
        Podemos obtener su valor asignandole una variable y un valor. Usariamos estos parametros:
            variable=varX, value=1
        De este modo podriamos concatenarlo a una funcion que nos indique si el valor que hay es 1 o otro(dependiendo de la cantidad de Radiobuttons que haiga)

    variable:
        Se utiliza para almacenar un valor cuando el objeto este seleccionado. Ej:
            variable=var1

    onvalue:
        Con este parametro podemos retornar un valor a la variable asociada cuando la casilla se encuentre
        activada. Ej:
            onvalue=True; onvalue=1
    
    offvalue:
        Con este parametro podemos retornar un valor a la variable asociada cuando la casilla se encuentre
        inactiva. Ej:
            offvalue=False; offvalue=2

"""
