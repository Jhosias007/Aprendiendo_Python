from tkinter import *
import time

raiz = Tk()
raiz.title("CPS")
frame = Frame(raiz, width=200, height=200)
frame.pack()

segundos = 0
detenerContador = False
clics = 0

def tiempo():
    global segundos
    global detenerContador

    time.sleep(1)
    segundos += 1

    if segundos == 10:
        detenerContador = True
        finalizarClics()


def finalizarClics():
    pass


def cuentaClics():
    global clics

    clics += 1





raiz.mainloop()
