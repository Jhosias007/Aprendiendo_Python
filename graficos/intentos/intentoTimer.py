from tkinter import *

raiz = Tk()
frame = Frame(raiz, width=200, height=400)
frame.pack()

comenzar = True
tiempo = StringVar()
tiempo.set("0")

# Funciones:

proceso = ""


def aumentarContador():
    global tiempo
    global comenzar
    global proceso

    # botonPrincipal.configure()

    tiempo.set(int(tiempo.get()) + 1)

    if tiempo.get() < 10:
        raiz.after(100, aumentarContador())


    if tiempo.get() == "10":
        #comenzar = False
        timer.after_cancel(aumentarContador())
        botonPrincipal.configure(text="Se ha acabado el tiempo", state="disabled")

    

botonPrincipal = Button(frame, width=30, height=5,
                        text="Click Aquí!", command=lambda: aumentarContador())
botonPrincipal.grid(row=1, column=1)

timer = Label(frame, width=30, height=5, textvariable=tiempo)
timer.grid(row=2, column=1)


raiz.mainloop()
