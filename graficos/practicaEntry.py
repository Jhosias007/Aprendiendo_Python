from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack()

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 3, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*", fg = "red")

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 4, column = 1, padx = 10, pady = 10)

srcollVert = Scrollbar(miFrame, command = textoComentario.yview)
srcollVert.grid(row = 4, column = 2, sticky = "nsew")
textoComentario.config(yscrollcommand = srcollVert.set, cursor = "crosshair", )


nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

apellidoLabel = Label(miFrame, text = "Apellido: ")
apellidoLabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

direccionLabel = Label(miFrame, text = "Direccion: ")
direccionLabel.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

direccionLabel = Label(miFrame, text = "Password: ")
direccionLabel.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)

comentariosLabel = Label(miFrame, text = "Comentarios: ")
comentariosLabel.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10)


botonEnviar = Button(raiz, text = "Enviar")
botonEnviar.grid()

raiz.mainloop()

"""
Entry es como un label pero para ingresar cuadros de texto para el usuario

Sintaxis:
cuadroDeTexto = Entry(raiz/frame)

Metodos:
 - .grid() =	Permite posicionar un Label o un Entry en el Frame, este crea cuadros y nosotros le indicamos el cuadro para poner el objeto
				Parametros:	Este recibe 2 parametros que son: (row = x, column = y), esto le indica la fila y columna en donde debe colocar el objeto indicado
							(sticky = "e") Este se tiene que igualar a un punto cardina e indica la posicion del width dentro de el cuadro
							El (pad = x) permite modificar la distancia desde el contenido de un width hasta los limites del mismo contenedor en px
							(padx = 10) El "padx" permite modificar el eje X, es decir los lados horizontales
							(pady = 10) El "pady" permite modificar el eje Y, es decir los lados verticales
"""
