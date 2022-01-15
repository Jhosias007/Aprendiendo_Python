from tkinter import *

raiz = Tk()

raiz.title("Interfaces Graficas")

#raiz.resizable(True, False)

#raiz.iconbitmap("rutaDelArchivo.ico")

#raiz.geometry("850x520")

raiz.config(bg = "green")

miFrame = Frame()

miFrame.pack(side = "left")

miFrame.config(bg = "red")

miFrame.config(width = "650", height = "350")

raiz.mainloop()

#43 https://www.youtube.com/watch?v=M80CzDC1Crc&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=43

"""
Tkinter es una libreria que se usa para crear interfaces graficas
Para crear una ventana solo ponemos el nombre y le decimos que es igual a Tk(), como crear un objeto

Metodos de Tkinter:
ejemplo.mainloop() = Se encarga de mantener abierta la ventana (Siempre se pone al final)
ejemplo.title() = Recibe un valor str y se encarga de cambiar el titulo
ejemplo.resizable() =	Recibe 2 valores booleanos y dependiendo de lo que ingresemos, podremos o no cambiar las 
						dimenciones de la pestaña en ejecucion
ejemplo.iconbitmap() = Recibe una ruta en str de un archivo .ico para poner como icono en la ventana
ejemplo.geometry() = Recibe 2 valores en un mismo str separados por una "x", se encarga de dar las dimensiones de la ventana
ejemplo.config() = Podemos configurar la ventana, por ejemplo, su color u otros

"""