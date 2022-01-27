from tkinter import *

raiz = Tk()

raiz.title("Python")

raiz.resizable(True, True)

#raiz.iconbitmap(ruta.ruta)

#raiz.geometry("350x350")

raiz.config(bg = "blue")

raiz.config(bd = "35", relief = "sunken")

raiz.config(cursor = "pirate")

#Frame

miFrame = Frame()

#miFrame.pack(side = "left", anchor = "n")

#miFrame.pack(fill = "both", expand = "True")

miFrame.pack()

miFrame.config(width = "350", height = "350")

miFrame.config(bg = "red")

miFrame.config(bd = "25", relief = "groove")

miFrame.config(cursor = "hand2")

raiz.mainloop()


"""
Para trabajar con interfaces graficas se necesitan librerias como Tkinter
Las ventanas estan formadas por una Raiz, la raiz contiene un Frame, y dentro del Frame hay varios widgets,
ya sean botones, contenedores de textos, etc.
En realidad todos los elementos (Raiz y Frame) son widgets pero se les puede llamar contenedores

Para crear una Raiz hacemos lo siguiente:
 - nombreRaiz = Tk()

Para crear un Frame hacemos lo siguiente:
 - nombreFrame = Frame()

La libreria Tkinter tiene varios eventos
Metodos de la Raiz:
- .mainloop() = Mantiene activa (se suele poner al final de todos los metodos de Tkinter)
- .title() = Le da un titulo a la ventatna (Este se escribe entre comillas)
- .resizable() = Indica si se puede redimencionar el tamaño de la ventana en ejecucion (recibe 2 valores bool)
- .iconbitmap() = Este cambia la foto del icono que aparece en la ventana (recibe la ruta del archivo .ico entre comillas)
- .geometry() = Cambia el tamaño de la ventana en pixeles (Recibe un valor en comillas como el siguiente: ("20x20"))
- .config() = Permite configurar varios aspectos de la ventana

Metodos del Frame:
- .pack() = De este modo empaquetamos el Frame dentro de la Raiz
- .config() = Permite configurar varios aspectos de la ventana

Opciones de empaquetado de Frame:
Estas opciones tienen que ir en los parentesis de la linea de empaquetado del Frame
- side = "right / left / up / bottom" = Hace que el Frame quede pegado a donde le indiques. No puedes poner 2 side
- anchor = "n / s / e / w" = Hace que el frame quede donde le indiquemos (norte, sur, este, oeste)
- fill = "x / y / both" =	Rellena de acuerdo a lo indicado cuando se modifica el tamaño de la ventana en ejecucion. 
							Tiene que ir acompañado de un: expand = "True"

Metodo .config():
- .config(bg = "color") = Le da color a lo indicado (Raiz o Frame)
- .config(width = "120", height = "120") = Le da tamaño en pixeles a lo indicado
- .config(relief = "groove") = Le da un tipo de borde
- .config(bd = "25") = Le da un tamaño al borde
- .config(cursor = "hand2") = Cambia el cursor al pasar por el lado indicado
"""