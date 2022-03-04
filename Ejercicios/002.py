import tkinter as tk
from tkinter import StringVar, messagebox
import sqlite3
import time


class App:
    # ? Variables
    varFila = 2

    diccionarioAlmacenaLabels = dict()

    listaDeClaves_id = list()
    listaDeClaves_nombre = list()
    listaDeClaves_nota = list()

    listaDeValores_id = list()
    listaDeValores_nombre = list()
    listaDeValores_nota = list()

    contadorParaCrearLabel = int()

    nombre_LabelId = str()
    nombre_LabelNombre = str()
    nombre_LabelNota = str()

    contadorParaNombre_LabelId = 0

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

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.obtenerIdParaCargar = self.cursorDeBase.fetchall()

        self.cursorDeBase.execute("SELECT nombre FROM alumnos")
        self.obtenerNombreParaCargar = self.cursorDeBase.fetchall()

        self.cursorDeBase.execute("SELECT nota FROM alumnos")
        self.obtenerNotaParaCargar = self.cursorDeBase.fetchall()

        # Capturo los datos del id en la lista correspondiente
        for i in self.obtenerIdParaCargar:
            self.listaDeClaves_id.append(
                int(str(i).replace(")", "").replace("(", "").replace(",", "")))
        print(self.listaDeClaves_id)

        # Capturo los datos de los nombres en la lista correspondiente
        for i in self.obtenerNombreParaCargar:
            self.listaDeClaves_nombre.append(str(i).replace(")", "").replace(
                "(", "").replace("'", "").replace(",", ""))
        print(self.listaDeClaves_nombre)

        # Capturo los datos de la nota en la lista correspondiente
        for i in self.obtenerNotaParaCargar:
            self.listaDeClaves_nota.append(
                int(str(i).replace(")", "").replace("(", "").replace(",", "")))
        print(self.listaDeClaves_nota)


        # * Creo los labels
        # ! tengo que conseguir que labelId se almacene en una lista o lo que sea
        # ! y en ves de ese entre otra variable

        a = "labelId"
        b = 1
        diccionario = {}

        diccionario[a + str(b)] = str(b)

        print(diccionario)

        for labelId in self.listaDeClaves_id:
            
            labelId = tk.Label(
                self.root, text=self.listaDeClaves_id[self.contadorParaCrearLabel])
            labelId.grid(row=self.varFila, column=0)

            self.varFila += 1
            self.contadorParaCrearLabel += 1

        labelId.destroy()
        
        self.varFila = 2
        self.contadorParaCrearLabel = 0

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
