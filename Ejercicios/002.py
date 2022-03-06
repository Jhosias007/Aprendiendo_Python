import tkinter as tk
from tkinter import StringVar, messagebox
import sqlite3


class App:
    # ? Variables
    varFila = 2

    # * Lo siguiente es para cargar los datos de la base a la app cuando se inicia
    diccionarioAlmacenaLabels = dict()

    listaDeClaves_id = list()
    listaDeClaves_nombre = list()
    listaDeClaves_nota = list()

    listaDeValores_id = list()
    listaDeValores_nombre = list()
    listaDeValores_nota = list()

    nombre_LabelId = "labelId"
    nombre_LabelNombre = "labelNombre"
    nombre_LabelNota = "labelNota"

    contadorParaNombre_LabelId = 1
    posicionDeLabel = 0

    # * Lo siguiente es para agregar un nuevo alumno

    listaNuevoAlumno = list()

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

    # * Funciones de botones principales

    def generarRootAñadirAlumno(self):
        self.rootAñadirAlumno = tk.Tk()

        # * Labels del rootAñadirAlumno (no necesitan declararse)
        tk.Label(self.rootAñadirAlumno, text="Añadir Alumno").grid(
            row=0, column=0, columnspan=2, padx=7, pady=7)
        tk.Label(self.rootAñadirAlumno, text="Nombre").grid(
            row=1, column=0, padx=7, pady=7)
        tk.Label(self.rootAñadirAlumno, text="Nota").grid(
            row=2, column=0, padx=7, pady=7)

        # * Entrys del rootAñadirAlumno
        self.nombre_AñadirAlumnoRoot_SV = StringVar()
        self.entryNombre_AñadirAlumnoRoot = tk.Entry(
            self.rootAñadirAlumno, textvariable=self.nombre_AñadirAlumnoRoot_SV)
        self.entryNombre_AñadirAlumnoRoot.grid(row=1, column=1, padx=7, pady=7)

        self.nota_AñadirAlumnoRoot_SV = StringVar()
        self.entryNota_AñadirAlumnoRoot = tk.Entry(
            self.rootAñadirAlumno, textvariable=self.nota_AñadirAlumnoRoot_SV)
        self.entryNota_AñadirAlumnoRoot.grid(row=2, column=1, padx=7, pady=7)

        # * Boton Guardar

        self.botonGuardar_AñadirAlumnoRoot = tk.Button(
            self.rootAñadirAlumno, text="Guardar", command=lambda: self.guardarAlumnoFuncion())
        self.botonGuardar_AñadirAlumnoRoot.grid(
            row=3, column=0, columnspan=2, padx=7, pady=7)

        self.rootAñadirAlumno.mainloop()

    def guardarAlumnoFuncion(self):
        # * Conexion a base y creacion de cursor y tabla
        self.conexionDeBase = sqlite3.connect("Base_002.db")

        self.cursorDeBase = self.conexionDeBase.cursor()
        self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (20),
            nota INTEGER
        )''')

        self.listaNuevoAlumno.append(
            str(self.entryNombre_AñadirAlumnoRoot.get()))
        self.listaNuevoAlumno.append(
            int(self.entryNota_AñadirAlumnoRoot.get()))

        self.cursorDeBase.execute(
            "INSERT INTO alumnos VALUES (NULL, ?, ?)", self.listaNuevoAlumno)

        # * Obtengo los ID's para dar la informacion

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.listaCapturarIdParaMessagebox = self.cursorDeBase.fetchall()
        self.ultimoIdParaMostrar = str(
            self.listaCapturarIdParaMessagebox.pop())
        self.ultimoIdParaMostrar = self.ultimoIdParaMostrar.replace(
            "(", "").replace(")", "").replace(",", "")

        self.rootAñadirAlumno.destroy()
        self.conexionDeBase.commit()
        self.listaNuevoAlumno.clear()

        messagebox.showinfo(
            "Nuevo Alumno", "Se ha registrado al alumno con el ID: " + self.ultimoIdParaMostrar )

        self.mostrarAlumnoAñadidoEnApp()

    def mostrarAlumnoAñadidoEnApp(self):
        pass #! tengo crear labels declarados que se generen segun los añadidos

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
        # print(self.listaDeClaves_id)

        # Capturo los datos de los nombres en la lista correspondiente
        for i in self.obtenerNombreParaCargar:
            self.listaDeClaves_nombre.append(str(i).replace(")", "").replace(
                "(", "").replace("'", "").replace(",", ""))
        # print(self.listaDeClaves_nombre)

        # Capturo los datos de la nota en la lista correspondiente
        for i in self.obtenerNotaParaCargar:
            self.listaDeClaves_nota.append(
                int(str(i).replace(")", "").replace("(", "").replace(",", "")))
        # print(self.listaDeClaves_nota)

        # * Creo los labels de ID

        for i in self.listaDeClaves_id:
            self.diccionarioAlmacenaLabels[self.nombre_LabelId + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_id[self.posicionDeLabel])
            self.diccionarioAlmacenaLabels[self.nombre_LabelId + str(
                self.contadorParaNombre_LabelId)].grid(row=self.varFila, column=0)

            self.varFila += 1
            self.contadorParaNombre_LabelId += 1
            self.posicionDeLabel += 1

        self.contadorParaNombre_LabelId = 1
        self.posicionDeLabel = 0
        self.varFila = 2

        # * Creo los labels de Nombre
        for i in self.listaDeClaves_nombre:
            self.diccionarioAlmacenaLabels[self.nombre_LabelNombre + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_nombre[self.posicionDeLabel])
            self.diccionarioAlmacenaLabels[self.nombre_LabelNombre + str(
                self.contadorParaNombre_LabelId)].grid(row=self.varFila, column=1)

            self.varFila += 1
            self.contadorParaNombre_LabelId += 1
            self.posicionDeLabel += 1

        self.contadorParaNombre_LabelId = 1
        self.posicionDeLabel = 0
        self.varFila = 2

        # * Creo los labels de Nota
        for i in self.listaDeClaves_nota:
            self.diccionarioAlmacenaLabels[self.nombre_LabelNota + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_nota[self.posicionDeLabel])
            self.diccionarioAlmacenaLabels[self.nombre_LabelNota + str(
                self.contadorParaNombre_LabelId)].grid(row=self.varFila, column=2)

            self.varFila += 1
            self.contadorParaNombre_LabelId += 1
            self.posicionDeLabel += 1


#        for i in self.diccionarioAlmacenaLabels:
#            print(i)

        # * Botones Principales
        self.generarGUI_BotonAñadirAlumno = tk.Button(
            self.root, text="Añadir Alumno", command=lambda: self.generarRootAñadirAlumno())
        self.generarGUI_BotonAñadirAlumno.grid(
            row=self.varFila, column=0, padx=7, pady=7)

        self.generarGUI_BotonEliminarAlumno = tk.Button(
            self.root, text="Eliminar Alumno")
        self.generarGUI_BotonEliminarAlumno.grid(
            row=self.varFila, column=2, padx=7, pady=7)

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
