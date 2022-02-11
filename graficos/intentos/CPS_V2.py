from tkinter import *


class ventana():
    def __init__(self):
        self.root = Tk()
        self.root.title("CPS Test V2")
        self.frame = Frame(self.root, width=200, height=200)
        self.generarBotones(self.frame)
        self.root.mainloop()

    def generarBotones(self, frameID):
        self.botonPrincipal = Button(frameID, width=20, height=10, text="Asd")
        self.botonPrincipal.grid(row=1, column=0)

app = ventana()
