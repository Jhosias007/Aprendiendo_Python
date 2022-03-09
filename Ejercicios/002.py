import tkinter as tk
from tkinter import StringVar, messagebox
import sqlite3
from tkinter.tix import COLUMN


class App:
    # ? Variables
    varFila = 2

    # * Lo siguiente es para cargar los datos de la base a la app cuando se inicia
    diccionarioAlmacenaLabels = dict()

    listaDeClaves_id = list()
    listaDeClaves_nombre = list()
    listaDeClaves_nota = list()

    nombre_LabelId = "labelId"
    nombre_LabelNombre = "labelNombre"
    nombre_LabelNota = "labelNota"

    posicionDeLabel = 0
    contadorParaNombre_LabelId = 1

    # * Lo siguiente es para mostrar al nuevo alumno en app
    diccionarioMostrarNewAlumno_ID = dict()
    diccionarioMostrarNewAlumno_Nombre = dict()
    diccionarioMostrarNewAlumno_Nota = dict()

    contadorParaPosicionarNewAlumno = 0

    nombreNewAl_LabelId = "labelId"
    nombreNewAl_LabelNombre = "labelNombre"
    nombreNewAl_LabelNota = "labelNota"

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
    # * Funciones de boton añadir alumno
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

        self.listaNuevoAlumno = list()

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

        messagebox.showinfo(
            "Nuevo Alumno", "Se ha registrado al alumno con el ID: " + self.ultimoIdParaMostrar)

        # * Obtengo valores para pasar por parametros a la funcion que mustra al new alumno en app

        # * Obtengo Id
        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.idAMostrar = int(str(self.cursorDeBase.fetchall().pop()).replace(
            "(", "").replace(")", "").replace(",", ""))

        # * Obtengo el Nombre
        self.cursorDeBase.execute("SELECT nombre FROM alumnos")
        self.nombreAMostrar = str(self.cursorDeBase.fetchall().pop()).replace(
            "(", "").replace(")", "").replace(",", "").replace("'", "")

        # * Obtengo la Nota
        self.cursorDeBase.execute("SELECT nota FROM alumnos")
        self.notaAMostrar = int(str(self.cursorDeBase.fetchall().pop()).replace(
            "(", "").replace(")", "").replace(",", ""))

        self.mostrarAlumnoAñadidoEnApp(
            self.idAMostrar, self.nombreAMostrar, self.notaAMostrar)

    def mostrarAlumnoAñadidoEnApp(self, id, nombre, nota):

        # * Obtengo el valor de varFila

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.varFila = int(len(self.cursorDeBase.fetchall())) + 2

        # * Agrego El ID
        self.diccionarioMostrarNewAlumno_ID[self.nombreNewAl_LabelId +
                                            str(id)] = tk.Label(self.root, text=id)

        self.diccionarioMostrarNewAlumno_ID[self.nombreNewAl_LabelId +
                                            str(id)].grid(row=self.varFila, column=0)

        # * Agrego Los Nombres
        self.diccionarioMostrarNewAlumno_Nombre[self.nombreNewAl_LabelNombre + str(
            id)] = tk.Label(self.root, text=nombre)
        self.diccionarioMostrarNewAlumno_Nombre[self.nombreNewAl_LabelNombre + str(
            id)].grid(row=self.varFila, column=1)

        # * Agrego Las Notas
        self.diccionarioMostrarNewAlumno_Nota[self.nombreNewAl_LabelNota + str(
            id)] = tk.Label(self.root, text=nota)
        self.diccionarioMostrarNewAlumno_Nota[self.nombreNewAl_LabelNota + str(
            id)].grid(row=self.varFila, column=2)

        self.varFila += 1

        # * Posicion de botones
        self.generarGUI_BotonAñadirAlumno.grid(row=self.varFila, column=0)
        self.generarGUI_BotonEliminarAlumno.grid(row=self.varFila, column=2)

    # * Funciones de boton eliminar alumno
    def generarRootEliminarAlumno(self):
        self.rootEliminarAlumno = tk.Tk()
        self.rootEliminarAlumno.title("Eliminar Alumno")

        # * Labels principales
        tk.Label(self.rootEliminarAlumno, text="Eliminar Alumno").grid(row=0, column=0, columnspan=2, padx=7, pady=7)
        tk.Label(self.rootEliminarAlumno, text="ID del Alumno").grid(row=1, column=0, padx=7, pady=7)

        # * Entrys principales
        self.entryID_EliminarAlumnoRoot_SV = StringVar()
        self.entryID_EliminarAlumnoRoot = tk.Entry(self.rootEliminarAlumno, textvariable=self.entryID_EliminarAlumnoRoot_SV)
        self.entryID_EliminarAlumnoRoot.grid(row=1, column=1, padx=7, pady=7)

        # * Botones principales
        self.buttonEnviar_EliminarAlumnoRoot = tk.Button(self.rootEliminarAlumno, text="Enviar", command=lambda: self.eliminarAlumnoFuncion())
        self.buttonEnviar_EliminarAlumnoRoot.grid(row=2, column=0, columnspan=2, padx=7, pady=7)

        self.rootEliminarAlumno.mainloop()

    def eliminarAlumnoFuncion(self):

        self.conexionDeBase = sqlite3.connect("Base_002.db")

        self.cursorDeBase = self.conexionDeBase.cursor()
        self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (20),
            nota INTEGER
        )''')

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.consultarIdsParaBorrarAl = str(self.cursorDeBase.fetchall()).replace("(", "").replace(",)", "")

        self.idDeAlumnoAEliminar = self.entryID_EliminarAlumnoRoot.get()

        if self.idDeAlumnoAEliminar in self.consultarIdsParaBorrarAl:
            self.cursorDeBase.execute("DELETE FROM alumnos WHERE id=?", self.idDeAlumnoAEliminar)
            self.rootEliminarAlumno.destroy()
            messagebox.showinfo("Alumno Eliminado", "Se ha eliminado el alumno correctamente")
        else:
            messagebox.showerror("ID Alumno", "El ID ingresado no existe")

        self.conexionDeBase.commit()

        self.quitarAlumnoDeApp(self.idDeAlumnoAEliminar)

    def quitarAlumnoDeApp(self, id):
        print(self.diccionarioAlmacenaLabels)
        print()
        print()

    def generarGUI(self):
        # * Labels Principales
        tk.Label(self.root, text="ALUMNOS").grid(row=0, column=1)
        tk.Label(self.root, text="ID").grid(row=1, column=0, padx=7, pady=7)
        tk.Label(self.root, text="Nombre").grid(row=1, column=1)
        tk.Label(self.root, text="Nota").grid(row=1, column=2, padx=7, pady=7)

        # * A partir de aqui empiezo a cargar los registros de la Base a la App

        # * Obtengo toda la informacion de la base separados
        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.obtenerIdParaCargar = self.cursorDeBase.fetchall()

        self.cursorDeBase.execute("SELECT nombre FROM alumnos")
        self.obtenerNombreParaCargar = self.cursorDeBase.fetchall()

        self.cursorDeBase.execute("SELECT nota FROM alumnos")
        self.obtenerNotaParaCargar = self.cursorDeBase.fetchall()

        # * Capturo los datos del id en la lista correspondiente
        for i in self.obtenerIdParaCargar:
            self.listaDeClaves_id.append(
                int(str(i).replace(")", "").replace("(", "").replace(",", "")))

        # * Capturo los datos de los nombres en la lista correspondiente
        for i in self.obtenerNombreParaCargar:
            self.listaDeClaves_nombre.append(str(i).replace(")", "").replace(
                "(", "").replace("'", "").replace(",", ""))

        # * Capturo los datos de la nota en la lista correspondiente
        for i in self.obtenerNotaParaCargar:
            self.listaDeClaves_nota.append(
                int(str(i).replace(")", "").replace("(", "").replace(",", "")))

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

        # * Botones Principales
        self.generarGUI_BotonAñadirAlumno = tk.Button(
            self.root, text="Añadir Alumno", command=lambda: self.generarRootAñadirAlumno())
        self.generarGUI_BotonAñadirAlumno.grid(
            row=self.varFila, column=0, padx=7, pady=7)

        self.generarGUI_BotonEliminarAlumno = tk.Button(
            self.root, text="Eliminar Alumno", command=lambda: self.generarRootEliminarAlumno())
        self.generarGUI_BotonEliminarAlumno.grid(
            row=self.varFila, column=2, padx=7, pady=7)

        self.conexionDeBase.commit()
        self.conexionDeBase.close()

        self.contadorParaNombre_LabelId = 1

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
