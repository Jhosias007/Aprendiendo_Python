from tkinter import *

root = Tk()

varOpcion = IntVar()


def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text="Masculino")

    elif varOpcion.get() == 2:
        etiqueta.config(text="Femenino")


Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion,
            value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion,
            value=2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()


"""

Radiobutton:
    Los Radiobutton se usan para marcar una opcion entre varias, podemos obtener el valor seleccionado 
    con el parametro "value" y podemos asignarle un comando con "command"
    
    Sintaxis:
        ejemploRadioButton = Radiobutton(root, text="Hola", variable=var1, value=1, *)
    
    Cuando la casilla es seleccionada, se almacena lo que haiga en el parametro value dentro de la
    variable indicada en los parametros. De este modo y con una funcion en cada Radiobutton podremos
    hallar que casilla esta seleccionada

    Lo que hay en value se almacena en la variable asociada

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
"""