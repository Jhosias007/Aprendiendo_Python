from cProfile import label
from pydoc import cli
from tkinter import *
import time
from turtle import color

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
dandoClicks = StringVar()
dandoClicks.set("0")

# ---------- Funciones ----------


def iniciarIntetno():
    accionClick()
    promedioClicks()
    timerAccion()

    if tiempoPasado == 10:
        finalizarIntento()


def finalizarIntento():
    pass


def timerAccion():
    global tiempoPasado
    global tiempoLimite

    while tiempoLimite < tiempoPasado:
        time.sleep(1)
        tiempoPasado += 1


def sacarScore():
    pass


def promedioClicks():
    pass


def accionClick():
    global dandoClicks
    

    dandoClicks = int(dandoClicks) + 1
    

# ---------- Botones ----------


botonPrincipal = Button(frame, width=35, height=10,
                        text="Click Para Empezar", command=lambda: [sacarScore(), accionClick()])
botonPrincipal.grid(row=2, column=1, columnspan=3)

botonReiniciar = Button(frame, width=35, height=2, text="Reiniciar")
botonReiniciar.grid(row=4, column=1, columnspan=3)

# ---------- Labels ----------

titulo = Label(frame, width=35, height=2, text="Prueba De CPS", fg="red")
titulo.grid(row=1, column=1, columnspan=3)

# ---------- Labels Esadisticos ----------

timer = Label(frame, width=10, height=2, text="Timer")
timer.grid(row=3, column=1)

clicksPS = Label(frame, width=10, height=2, textvariable=dandoClicks, text=dandoClicks)
clicksPS.grid(row=3, column=2)

score = Label(frame, width=10, height=2, text="Score")
score.grid(row=3, column=3)

raiz.mainloop()
