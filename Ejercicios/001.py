from tkinter import *
from tkinter import messagebox
import sqlite3


class App():
    def __init__(self):
        # ? Crear root
        self.root = Tk()
        self.root.title("Alumnos")

        # ? Funciones llamadas
        self.generarMenu()
        self.generarPlantilla()
        self.root.mainloop()

        # ? Variables
        self.varConectarseBool = False

    # * Funciones - Menu

    def funcionConectarseMenu(self):
        # ? Conexion a SQLite3
        try:
            self.conexion = sqlite3.connect("Base.db")
            self.cursor = self.conexion.cursor()
            self.cursor.execute('''CREATE TABLE ALUMNOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR (50),
                NOTA INTEGER
            )''')
            self.varConectarseBool = True

            messagebox.showinfo(
                "Conexion", "Te has conectado a la Base de Datos exitosamente")

        except sqlite3.OperationalError:
            messagebox.showerror(
                "Conexion", "Ya estas conectado a la base de datos")

        self.conexion.commit()

    def salirMenuFuncion(self):
        self.cerrarApp = messagebox.askyesno(
            "Salir", "¿Deseas salir de la aplicacion?")
        if self.cerrarApp == YES:
            self.root.destroy()

    # * Funciones de añadir alumno
    def añadirAlumnoRoot(self):

        self.rootAñadirAlumno = Tk()

        self.labelTituloAñadirAlumno = Label(
            self.rootAñadirAlumno, text="Añadir Alumno")
        self.labelTituloAñadirAlumno.grid(row=0, column=0, columnspan=2)

        self.labelNombreAñadirAlumno = Label(
            self.rootAñadirAlumno, text="Nombre: ")
        self.labelNombreAñadirAlumno.grid(row=1, column=0, padx=10, pady=10)

        self.labelNotaAñadirAlumno = Label(
            self.rootAñadirAlumno, text="Nota: ")
        self.labelNotaAñadirAlumno.grid(row=2, column=0, padx=10, pady=10)

        self.stringVarNombreAñadirAlumno = StringVar()
        self.entryNombreAñadirAlumno = Entry(
            self.rootAñadirAlumno, textvariable=self.stringVarNombreAñadirAlumno)
        self.entryNombreAñadirAlumno.grid(row=1, column=1, padx=10, pady=10)

        self.stringVarNotaAñadirAlumno = StringVar()
        self.entryNotaAñadirAlumno = Entry(
            self.rootAñadirAlumno, textvariable=self.stringVarNotaAñadirAlumno)
        self.entryNotaAñadirAlumno.grid(row=2, column=1, padx=10, pady=10)

        self.buttonEnviarAñadirAlumno = Button(
            self.rootAñadirAlumno, text="Guardar Alumno", command=lambda: self.guardarAlumnoEnBase()
        )

        self.buttonEnviarAñadirAlumno.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

        self.rootAñadirAlumno.mainloop()

    def guardarAlumnoEnBase(self):
        # try:
        if self.entryNombreAñadirAlumno.get().isalpha() == False:
            messagebox.showerror(
                "Error", "No puedes colocar un numero u otros digitos en el nombre")
            self.rootAñadirAlumno.mainloop()

        if self.entryNotaAñadirAlumno.get().isdigit() == False:
            messagebox.showerror(
                "Error", "Solo debes colocar numeros en la nota")
            self.rootAñadirAlumno.mainloop()

        if int(self.entryNotaAñadirAlumno.get()) < 0:
            messagebox.showerror("Nota", "No puedes colocar numeros negativos")
            self.rootAñadirAlumno.mainloop()

        if int(self.entryNotaAñadirAlumno.get()) > 20:
            messagebox.showerror("Nota", "El limite de la nota es 20")
            self.rootAñadirAlumno.mainloop()

        self.infoAlumnoAñadir = (
            str(self.entryNombreAñadirAlumno.get()),
            int(self.entryNotaAñadirAlumno.get())
        )

        self.conexion = sqlite3.connect("Base.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''
                INSERT INTO ALUMNOS VALUES (NULL, ?, ?)''', self.infoAlumnoAñadir)

        self.cursor.execute("SELECT ID FROM ALUMNOS")
        self.capturarID = self.cursor.fetchall()
        self.ultimoID = str(self.capturarID.pop())

        self.ultimoID = self.ultimoID.replace("(", "")
        self.ultimoID = self.ultimoID.replace(")", "")
        self.ultimoID = self.ultimoID.replace(",", "")

        self.conexion.commit()
        self.rootAñadirAlumno.destroy()

        messagebox.showinfo(
            "Alumno Añadido", "Se ha cargado el alumno con ID: " + self.ultimoID)

        self.idAMostrar = "id_" + self.ultimoID + "_Label"
        self.nombreAMostrar = "nombre_" + self.infoAlumnoAñadir[0] + "_Nombre"
        self.notaAMostrar = "nota_" + str(self.infoAlumnoAñadir[1]) + "_Nota"
        # Este es el lugar inicial en donde se colocaran la informacion en la funcion
        self.varFila = 2
        # mostrarAlumnoAñadido()

        self.mostrarAlumnoAñadido(
            self.ultimoID,
            self.infoAlumnoAñadir[0],
            self.infoAlumnoAñadir[1],
        )
    
    def mostrarAlumnoAñadido(self, id, nombre, nota):
        try:
            # Me conecto a la base (otra vez)
            self.conexion = sqlite3.connect("Base.db")
            self.cursor = self.conexion.cursor()

            # Captura de datos

            self.cursor.execute("SELECT ID FROM ALUMNOS")
            self.cargarIdListaParaPosicionar = self.cursor.fetchall()

            self.varFila = str(self.cargarIdListaParaPosicionar.pop())
            self.varFila = self.varFila.replace("(", "")
            self.varFila = self.varFila.replace(")", "")
            self.varFila = self.varFila.replace(",", "")

            self.varFila = int(self.varFila) + 2

            Label(self.root, text=id).grid(row=self.varFila, column=0)
            Label(self.root, text=nombre).grid(row=self.varFila, column=1)
            Label(self.root, text=nota).grid(row=self.varFila, column=2)

            self.añadirAlumnoBoton.grid(row=self.varFila + 1)
            self.eliminarAlumnoDeBaseBoton.grid(row=self.varFila + 1)

        except TclError:
            pass

    # * Funciones de eliminar alumno
    def eliminarAlumnoRoot(self):
        self.rooteliminarAlumnoDeBase = Tk()
        self.rooteliminarAlumnoDeBase.title("Eliminar Alumno")

        self.tituloeliminarAlumnoDeBase = Label(
            self.rooteliminarAlumnoDeBase, text="Eliminar Alumno")
        self.tituloeliminarAlumnoDeBase.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10)

        self.idAlumnoBorrarLabel = Label(
            self.rooteliminarAlumnoDeBase, text="ID Del Alumno")
        self.idAlumnoBorrarLabel.grid(row=1, column=0, padx=10, pady=10)

        self.idAlumnoBorrarStringVar = StringVar()
        self.idAlumnoBorrarEntry = Entry(
            self.rooteliminarAlumnoDeBase, textvariable=self.idAlumnoBorrarStringVar)
        self.idAlumnoBorrarEntry.grid(row=1, column=1, padx=10, pady=10)

        self.idAlumnoBorrarBoton = Button(
            self.rooteliminarAlumnoDeBase, text="Aceptar", width=13, command=lambda: self.eliminarAlumnoDeBase())
        self.idAlumnoBorrarBoton.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10)

    def eliminarAlumnoDeBase(self):

        # * Me conecto a la base (otra vez)
        self.conexion = sqlite3.connect("Base.db")
        self.cursor = self.conexion.cursor()

        # * Obtener Datos para saber si el ID ingresado existe

        self.cursor.execute("SELECT ID FROM ALUMNOS")
        self.verificarIdExisteParaBorrar = self.cursor.fetchall()

        # * Recorrer la lista self.verificarIdExisteParaBorrar para ver si existe el id ingresado
        # * Corregir

#        if self.verificarIdExisteParaBorrar.__contains__(int(self.idAlumnoBorrarEntry.get())) == False:
#            messagebox.showerror("ID", "El ID ingresado no existe")
#            self.rooteliminarAlumnoDeBase.mainloop()

        self.idObtenidoABorrar = (int(self.idAlumnoBorrarEntry.get()), )

        self.cursor.execute("DELETE FROM ALUMNOS WHERE ID=?",
                            self.idObtenidoABorrar)
        self.conexion.commit()

        self.rooteliminarAlumnoDeBase.destroy()

        messagebox.showinfo(
            "Base de Datos", "El alumno se ha eliminado exitosamente")

    def eliminarAlumnoDeApp(self):
        pass

    # * Funciones - Ayuda
    def funcionLicencia(self):
        messagebox.showinfo("Licencia", "La licencia es mia, XD")

    def funcionAcercaDe(self):
        messagebox.showinfo("Acerca De", "Programa hecho por mi en este año")

    # * Funciones - Generar Ventana
    def generarMenu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.archivo = Menu(self.menu, tearoff=False)
        self.archivo.add_command(
            label="Conectarse", command=lambda: self.funcionConectarseMenu())
        self.archivo.add_separator()
        self.archivo.add_command(
            label="Salir", command=lambda: self.salirMenuFuncion())

        self.alumnos = Menu(self.menu, tearoff=False)
        self.alumnos.add_command(
            label="Agregar Alumno", command=lambda: self.añadirAlumnoRoot())
        self.alumnos.add_command(
            label="Eliminar Alumno", command=lambda: self.eliminarAlumnoRoot())
        self.alumnos.add_separator()
        self.alumnos.add_command(label="Ver Aprobados")
        self.alumnos.add_command(label="Ver Desaprobados")

        self.ayuda = Menu(self.menu, tearoff=False)
        self.ayuda.add_command(
            label="Licencia", command=lambda: self.funcionLicencia())
        self.ayuda.add_command(
            label="Acerca De", command=lambda: self.funcionAcercaDe())

        self.menu.add_cascade(menu=self.archivo, label="Archivo")
        self.menu.add_cascade(menu=self.alumnos, label="Alumnos")
        self.menu.add_cascade(menu=self.ayuda, label="Ayuda")

    def generarPlantilla(self):
        # * Labels
        self.labelTitulo = Label(self.root, text="ALUMNOS")
        self.labelTitulo.grid(row=0, column=1)

        # * Label Encabezado

        self.labelID = Label(self.root, text="ID Alumno:")
        self.labelID.grid(row=1, column=0, padx=10, pady=10)

        self.labelNombreAlumno = Label(self.root, text="Nombre")
        self.labelNombreAlumno.grid(row=1, column=1, padx=10, pady=10)

        self.labelNotaAlumno = Label(self.root, text="Nota")
        self.labelNotaAlumno.grid(row=1, column=2, padx=10, pady=10)

        # * Cargar datos de la base a la app

        # Me conecto a la base (otra vez)
        self.conexion = sqlite3.connect("Base.db")
        self.cursor = self.conexion.cursor()

        # Captura de datos

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ALUMNOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR (50),
                NOTA INTEGER
            )''')

        self.cursor.execute("SELECT ID FROM ALUMNOS")
        self.cargarIDLista = self.cursor.fetchall()

        self.cursor.execute("SELECT NOMBRE FROM ALUMNOS")
        self.cargarNombreLista = self.cursor.fetchall()

        self.cursor.execute("SELECT NOTA FROM ALUMNOS")
        self.cargarNotaLista = self.cursor.fetchall()

        # Aqui creo un label a cada vuelta de bucle que se recorre de la lista capturada con el fetchall
        
        self.varFila = 2

        for id in self.cargarIDLista:
            Label(self.root, text=id).grid(
                row=self.varFila, column=0, padx=3, pady=3)

            self.varFila += 1

        self.varFila = 2

        for nombre in self.cargarNombreLista:
            Label(self.root, text=nombre).grid(
                row=self.varFila, column=1, padx=3, pady=3)
            
            self.varFila += 1

        self.varFila = 2

        for nota in self.cargarNotaLista:
            Label(self.root, text=nota).grid(
                row=self.varFila, column=2, padx=3, pady=3)

            self.varFila += 1

        # Cargar los encabezados por partes, primero el id, luego el nombre y la nota al final

        # * Buttons

        self.añadirAlumnoBoton = Button(
            self.root, text="Añadir Alumno", command=lambda: self.añadirAlumnoRoot())
        self.añadirAlumnoBoton.grid(
            row=self.varFila, column=0, padx=10, pady=10)

        self.eliminarAlumnoDeBaseBoton = Button(
            self.root, text="Eliminar Alumno", command=lambda: self.eliminarAlumnoRoot())
        self.eliminarAlumnoDeBaseBoton.grid(
            row=self.varFila, column=2, padx=10, pady=10)


miApp = App()
