from tkinter import *
import time


raiz = Tk()
raiz.title("CPS TEST")
frame = Frame(raiz, width=200, height=200)
frame.pack()

# ---------- Variables Globales ----------


tiempoPasado = 0
tiempoLimite = 10
comenzarTimer = True

infoTimer = IntVar()
infoClicksPS = IntVar()
infoScore = IntVar()

# ---------- Funciones ----------


def finalizarIntento():
    botonPrincipal.configure(text="El tiempo ha acabado!", state="disabled")


def accionReinicar():
    global tiempoPasado
    global comenzarTimer

    tiempoPasado = 0
    comenzarTimer = False

    infoTimer.set(0)
    infoClicksPS.set(0)
    infoScore.set(0)

    botonPrincipal.configure(text="Click Para Empezar", state="normal")


def iniciarTimer():  # Corregir el inicio en 1
    global tiempoPasado
    global tiempoLimite
    global comenzarTimer

    botonPrincipal.configure(
        command=lambda: aumentarClicks(), text="Sigue Clickeando!")

    if comenzarTimer == True:
        tiempoPasado += 1
        infoTimer.set(infoTimer.get() + 1)

        if tiempoPasado == tiempoLimite:
            comenzarTimer = False
            finalizarIntento()
        raiz.after(1000, iniciarTimer)


def aumentarClicks():  # Acabado
    infoScore.set(infoScore.get() + 1)


def calcularScore():  # Terminar
    pass


def comenzarTiempo():
    global comenzarTimer
    comenzarTimer = True
    botonPrincipal.configure(text="Click Para Empezar", state="normal")


# ---------- Botones ----------

botonPrincipal = Button(frame, width=35, height=10,
                        text="Click Para Empezar", command=lambda: [aumentarClicks(), iniciarTimer(), calcularScore(), comenzarTiempo()])
botonPrincipal.grid(row=2, column=1, columnspan=3)

botonReiniciar = Button(frame, width=35, height=2,
                        text="Reiniciar", command=lambda: accionReinicar())
botonReiniciar.grid(row=4, column=1, columnspan=3)

# ---------- Labels ----------

titulo = Label(frame, width=35, height=2, text="Prueba De CPS", fg="red")
titulo.grid(row=1, column=1, columnspan=3)

# ---------- Labels Esadisticos ----------

timer = Label(frame, width=10, height=2, textvariable=infoTimer)
timer.grid(row=3, column=1)

clicksPS = Label(frame, width=10, height=2, textvariable=infoClicksPS)
clicksPS.grid(row=3, column=2)

score = Label(frame, width=10, height=2, textvariable=infoScore)
score.grid(row=3, column=3)


raiz.mainloop()
