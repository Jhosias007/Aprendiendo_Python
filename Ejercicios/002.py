import tkinter as tk
from tkinter import messagebox
import sqlite3


class App:
    # ? Variables
    varFila = 2

    def __init__(self):
        # * Acciones del root principal
        self.root = tk.Tk()
        self.root.title("El fin se aleja")

        # * Llamadas a funciones
        self.generarMenuGUI()
        self.generarGUI()
        self.root.mainloop()

    def generarGUI(self):
        # * Labels Principales
        tk.Label(self.root, text="ALUMNOS").grid(row=0, column=1)
        tk.Label(self.root, text="ID").grid(row=1, column=0, padx=7, pady=7)
        tk.Label(self.root, text="Nombre").grid(row=1, column=1)
        tk.Label(self.root, text="Nota").grid(row=1, column=2, padx=7, pady=7)

        # * Labels a cargar de la Base

        # completar

        # * Botones Principales
        self.generarGUI_BotonAñadirAlumno = tk.Button(
            self.root, text="Añadir Alumno")
        self.generarGUI_BotonAñadirAlumno.grid(
            row=self.varFila, column=0, padx=7, pady=7)

        self.generarGUI_BotonEliminarAlumno = tk.Button(
            self.root, text="Eliminar Alumno")
        self.generarGUI_BotonEliminarAlumno.grid(
            row=self.varFila, column=2, padx=7, pady=7)

    def generarMenuGUI(self):
        # * Creo el menu principal
        self.menuPrincipal = tk.Menu(self.root)
        self.root.config(menu=self.menuPrincipal)

        # * Creo sub menus
        self.menuArchivo = tk.Menu(self.menuPrincipal, tearoff=False)
        self.menuAlumnos = tk.Menu(self.menuPrincipal, tearoff=False)
        self.menuAyuda = tk.Menu(self.menuPrincipal, tearoff=False)

        # * Creo las opciones de los sub menus
        # Opciones del sub menu "menuArchivo"
        self.menuArchivo.add_command(label="Nueva Ventana")
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir")

        # Opciones del sub menu "menuAlumnos"
        self.menuAlumnos.add_command(label="Añadir Alumno")
        self.menuAlumnos.add_command(label="Eliminar Alumno")
        self.menuAlumnos.add_command(label="Editar Alumno")
        self.menuAlumnos.add_separator()
        self.menuAlumnos.add_command(label="Ver Aprobados")
        self.menuAlumnos.add_command(label="Ver Desaprobados")

        # Opciones del sub menu "menuAyuda"
        self.menuAyuda.add_command(label="Licencia")
        self.menuAyuda.add_command(label="Acerca De")

        # * Hago visible el menu principal y los sub menus
        self.menuPrincipal.add_cascade(menu=self.menuArchivo, label="Alumnos")
        self.menuPrincipal.add_cascade(menu=self.menuAlumnos, label="Archivo")
        self.menuPrincipal.add_cascade(menu=self.menuAyuda, label="Ayuda")


app_001 = App()

# ! Dia 2 de Marzo del 2022. Comienza Epicamente*
