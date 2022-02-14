from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero=filedialog.askopenfile(title="NUV")
    print(fichero)

Button(root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()
