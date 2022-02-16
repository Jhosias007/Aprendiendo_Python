from tkinter import *
import tkinter.scrolledtext as sc
from io import open


class App():

    def __init__(self):
        self.root = Tk()
        self.generarWidgets()
        self.root.mainloop()

    def generarWidgets(self):
        # SubTitulo
        self.subtitulo = Label(self.root, width=15,
                               text="Añadir Comentario", padx=10, pady=10)
        self.subtitulo.grid(row=0, column=1)

        # Entrada para el comentario
        self.introduceComentario = sc.ScrolledText(
            self.root, width=20, height=10, padx=10, pady=10, wrap=WORD)
        self.introduceComentario.grid(row=1, column=1)
        self.introduceComentario.focus()

        # Boton Enviar Comentario
        self.botonEnviar = Button(
            self.root, text="Enviar Comentario", command=self.funcEnviar)
        self.botonEnviar.grid(row=2, column=1)

    def funcEnviar(self):
        self.guardaComentario = open("GuardaComentario.txt", "w")
        self.contenidoComentario = self.introduceComentario.get("1.0", END)
        self.guardaComentario.write(self.contenidoComentario)
        self.guardaComentario.seek()
        self.guardaComentario.write("\n")

newApp = App()
