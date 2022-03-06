from ast import Delete
import tkinter as tk

root = tk.Tk()


botonDelete = tk.Button(root, text="Delete lbl1",
                        command=lambda: deleteLabel1())
botonDelete.grid(row=2, column=0)


lbl2 = tk.Label(root, text="nota")
lbl2.grid(row=1, column=0)

diccionario = {
    "lbl1": tk.Label(root, text="name")
}

diccionario["lbl1"].grid(row=0, column=0)

print(diccionario["lbl1"])


def deleteLabel1():
    diccionario["lbl1"].destroy()
    del diccionario["lbl1"]
    print(diccionario)


root.mainloop()
