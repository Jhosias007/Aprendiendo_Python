from tkinter import *

root = Tk()
root.title("Check Button")

frame = Frame(root, width=20)
frame.pack()




texto = Label(frame, text="Selecciona tu destino").pack()
Checkbutton(frame, text="Playa").pack()
Checkbutton(frame, text="Montaña").pack()
Checkbutton(frame, text="Turismo rural").pack()


root.mainloop()
#12