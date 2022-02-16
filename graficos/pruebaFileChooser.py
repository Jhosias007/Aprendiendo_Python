from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():
    fichero = filedialog.askopenfile(title="NUV", initialdir="C:", filetypes=(
        ("Ficheros de Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"), ("Todos los Ficheros", "*.*")))
    print(fichero)

#23
Button(root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()
