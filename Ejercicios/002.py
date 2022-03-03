import tkinter as tk
from tkinter import messagebox
import sqlite3
import time

class App:
    # ? Variables
    varFila = 2

    diccionarioAlmacenaLabels = dict()

    def __init__(self):
        # * Crear y modificar root principal
        self.root = tk.Tk()
        self.root.title("El fin se aleja")

        # * Conectarse a la Base de Datos y crear tabla con un cursor
        self.conexionDeBase = sqlite3.connect("Base_002.db")
        
        self.cursorDeBase = self.conexionDeBase.cursor()
        self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (20),
            nota INTEGER
        )''')

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

        # * A partir de aqui empiezo a cargar los registros de la Base a la App
        
        #self.cursorDeBase.execute("INSERT INTO alumnos VALUES (NULL, 'DIEGO', 20)")
        #self.cursorDeBase.execute("INSERT INTO alumnos VALUES (NULL, 'ALVARO', 15)")

        # Llamo a los "id" de la tabla "alumnos"

        self.cursorDeBase.execute("SELECT * FROM alumnos")
        self.obtenerDatosParaCargar = self.cursorDeBase.fetchall()

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.obtenerIdParaSeparar = self.cursorDeBase.fetchall()

        for i in self.obtenerDatosParaCargar:
            # * Con el siguiente "for" separo las listasy y poco mas
            for i in self.obtenerIdParaSeparar:
                self.labelIdentificador = "labelIdentificador_id" + str(self.obtenerIdParaSeparar.pop()).replace("(", "").replace(")", "").replace(",", "")
                print(self.labelIdentificador)

                self.labelValor = int(list(self.labelIdentificador).pop())
                print(self.labelValor)

                self.diccionarioAlmacenaLabels[self.labelIdentificador] = self.labelValor

        print(self.diccionarioAlmacenaLabels)
        #! almacenar el valor de self.labelIdentificar en un label. igual para el otro

        # * Botones Principales
        self.generarGUI_BotonAñadirAlumno = tk.Button(
            self.root, text="Añadir Alumno")
        self.generarGUI_BotonAñadirAlumno.grid(
            row=self.varFila + 1, column=0, padx=7, pady=7)

        self.generarGUI_BotonEliminarAlumno = tk.Button(
            self.root, text="Eliminar Alumno")
        self.generarGUI_BotonEliminarAlumno.grid(
            row=self.varFila + 1, column=2, padx=7, pady=7)

        self.conexionDeBase.commit()
        self.conexionDeBase.close()

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
