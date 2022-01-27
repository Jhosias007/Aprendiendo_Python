from tkinter import *

root = Tk()

miFrame = Frame(root, width = "500", height = "400")
miFrame.pack()

miLabel = Label(miFrame, text = "Hola mundo", fg = "red", font = ("Comic Sans MS", 20))
miLabel.place(x = 0, y = 0)

#Label(miFrame, text = "Hola mundo").place(x = 0, y = 0)
#De este modo lo unico que hacemos es crear un label pero no lo asignamos a nada, esto se usa cuando 
#El texto no se usara o modificara en un futuro (es un texto fijo).

miImagen = PhotoImage(file = "jijijija.png")
Label(miFrame, image = miImagen).place(x = 0, y = 10)

root.mainloop()


"""
Un label es un valor que ingresas, puede ser texto o imagen
Sintaxis:
nombreLabel = Label(contenedor, opciones)

Al declarar el label le pasamos 2 o mas parametros, el primero es al contenedor en el que se encontrará, 
y el en el segundo puedes poner un monton de opciones, por ejemplo, un texto o imagen.
Luego podras poner mas parametros de acuerdo a lo ingresado, por ejemplo: fg = "red" = cambia el color del texto a rojo

A la hora de empaquetar un label puede seguir el metodo normal pero el tamaño de la ventana se adaptara al texto.
Para este caso es mejor usar .place() que .pack()

Podemos crear un label sin asignarlo a una variable, esto se usa si no se modificara el valor del label despues

Sintaxis de .place():
nombreLabel.place(x = 100, y = 100)
Este metodo se encarga de que el label no adapte el tamaño de la ventana al texto y mas bien coloca el texto en la
posicion indicada por los parametros.

PhotoImage es una clase que se utiliza para manipular imagenes en la ventana
Sintaxis:
nombreImagen = PhotoImage(file = "ruta.png")
Este recibe como parametro la ruta como se muestra en el ejemplo
PhotoImage no tiene los metodos .label ni .place, por lo que no podremos modificar la imagen en un futuro

"""