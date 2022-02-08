from ast import Lambda
from tkinter import *
import time


raiz = Tk()
raiz.title("CPS TEST")
frame = Frame(raiz, width=200, height=200)
frame.pack()

# ---------- Variables Globales ----------


tiempoPasado = 0
promedioClicksEnAccion = 0
clicksFinales = 0
promedioClicksEnAccion = 0
tiempoLimite = 10
dandoClicks = 0

# ---------- Funciones ----------


def finalizarIntento():
    botonPrincipal.configure(text="El tiempo ha acabado!", state="disabled")


def iniciarTimer():
    global tiempoPasado
    global tiempoLimite

    tiempoPasado += 1
    timer.configure(text=tiempoPasado)

    if tiempoPasado == 10:
        finalizarIntento()
        raiz.after_cancel(iniciarTimer())

    raiz.after(1000, iniciarTimer())


def calcularScore():
    pass


def calcularClicks():
    pass


def aumentarClicks():
    global dandoClicks
    dandoClicks += 1
    # De este modo podemos variar el texto de un Label: label['text'] = "hola mundo"
    clicksPS["text"] = dandoClicks

# ---------- Botones ----------


botonPrincipal = Button(frame, width=35, height=10,
                        text="Click Para Empezar", command=lambda: [aumentarClicks(), iniciarTimer()])
botonPrincipal.grid(row=2, column=1, columnspan=3)

botonReiniciar = Button(frame, width=35, height=2, text="Reiniciar")
botonReiniciar.grid(row=4, column=1, columnspan=3)

# ---------- Labels ----------

titulo = Label(frame, width=35, height=2, text="Prueba De CPS", fg="red")
titulo.grid(row=1, column=1, columnspan=3)

# ---------- Labels Esadisticos ----------

timer = Label(frame, width=10, height=2, text=0)
timer.grid(row=3, column=1)

clicksPS = Label(frame, width=10, height=2, text=0)
clicksPS.grid(row=3, column=2)

score = Label(frame, width=10, height=2, text="Score")
score.grid(row=3, column=3)


raiz.mainloop()
