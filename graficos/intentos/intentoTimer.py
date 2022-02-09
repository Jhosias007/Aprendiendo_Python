from tkinter import *

raiz = Tk()
frame = Frame(raiz, width=200, height=400)
frame.pack()

comenzar = True
tiempo = IntVar()
tiempo.set(0)

# Funciones:

proceso = ""


def aumentarContador():
    global tiempo
    global comenzar
    global proceso

    if comenzar:
        botonPrincipal.configure(state="active")
        if tiempo.get() == 9:
            comenzar = False
            botonPrincipal.configure(text="Tiempo Acabado!", state="disabled")
        tiempo.set(tiempo.get() + 1)
        raiz.after(200, aumentarContador())


# Zona Botones

botonPrincipal = Button(frame, width=30, height=5,
                        text="Click Aquí!", command=lambda: aumentarContador())
botonPrincipal.grid(row=1, column=1)

timer = Label(frame, width=30, height=5, textvariable=tiempo)
timer.grid(row=2, column=1)


raiz.mainloop()
