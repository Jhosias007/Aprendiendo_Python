from tkinter import *
import sqlite3
from tkinter import messagebox


class App():
    def __init__(self):
        # ? Crear root
        self.root = Tk()
        self.root.title("Alumnos")

        # ? Funciones llamadas
        self.generarMenu()
        self.generarPlantilla()
        self.root.mainloop()

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

        except sqlite3.OperationalError:
            messagebox.showerror(
                "Conexion", "Ya estas conectado a la base de datos")

        self.conexion.commit()

    def salirMenuFuncion(self):
        self.cerrarApp = messagebox.askyesno(
            "Salir", "¿Deseas salir de la aplicacion?")
        if self.cerrarApp == YES:
            self.root.destroy()

    def añadirAlumnoFuncion(self):
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
            self.rootAñadirAlumno, text="Guardar Alumno", command=lambda: self.guardarAlumnoFuncion()
        )

        self.buttonEnviarAñadirAlumno.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

#        self.infoAlumnoAñadir = (
#            str(self.stringVarNombreAñadirAlumno.get()),
#            str(self.stringVarNotaAñadirAlumno.get())
#        )

        self.rootAñadirAlumno.mainloop()

    def guardarAlumnoFuncion(self):

        self.infoAlumnoAñadir = (
            str(self.stringVarNombreAñadirAlumno.get()),
            str(self.stringVarNotaAñadirAlumno.get())
        )

        print(self.infoAlumnoAñadir)

        self.conexion = sqlite3.connect("Base.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''
            INSERT INTO ALUMNOS VALUES (NULL, ?, ?)''', self.infoAlumnoAñadir)

        messagebox.showinfo("Alumno Añadido", "Se ha cargado el alumno")

        self.conexion.commit()
        self.rootAñadirAlumno.destroy()

    def eliminarAlumnoFuncion(self):
        pass

    def añadirAlumnoAApp(self, nombre, nota, principalLabel, nombreLabel, notaLabel):
        self.varFila = 2

        principalLabel = Label(self.root, text="Alumno:")
        principalLabel.grid(row=self.varFila, column=0, padx=10, pady=10)

        nombreLabel = Label(self.root, text=nombre)
        nombreLabel.grid(
            row=self.varFila, column=1, padx=10, pady=10)

        notaLabel = Label(self.root, text=nota)
        notaLabel.grid(
            row=self.varFila, column=2, padx=10, pady=10)

        self.varFila += 1

        self.añadirAlumnoBoton.grid(row=self.varFila + 1)
        self.eliminarAlumnoBoton.grid(row=self.varFila + 1)

    # * Funciones - Ventana

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
            label="Agregar Alumno", command=lambda: self.añadirAlumnoFuncion())
        self.alumnos.add_command(
            label="Eliminar Alumno", command=lambda: self.eliminarAlumnoFuncion())
        self.alumnos.add_separator()
        self.alumnos.add_command(label="Ver Aprobados")
        self.alumnos.add_command(label="Ver Desaprobados")

        self.ayuda = Menu(self.menu, tearoff=False)
        self.ayuda.add_command(label="Licencia")
        self.ayuda.add_command(label="Acerca De")

        self.menu.add_cascade(menu=self.archivo, label="Archivo")
        self.menu.add_cascade(menu=self.alumnos, label="Alumnos")
        self.menu.add_cascade(menu=self.ayuda, label="Ayuda")

    def generarPlantilla(self):

        # * Labels
        self.labelTitulo = Label(self.root, text="ALUMNOS")
        self.labelTitulo.grid(row=0, column=1)

        # * Label Encabezado
        self.varFila = 1

        self.labelAlumno = Label(self.root, text="Alumno:")
        self.labelAlumno.grid(row=self.varFila, column=0, padx=10, pady=10)

        self.labelNombreAlumno = Label(self.root, text="Nombre")
        self.labelNombreAlumno.grid(
            row=self.varFila, column=1, padx=10, pady=10)

        self.labelNotaAlumno = Label(self.root, text="Nota")
        self.labelNotaAlumno.grid(
            row=self.varFila, column=2, padx=10, pady=10)

        self.varFila += 1

        # * Buttons

        self.añadirAlumnoBoton = Button(
            self.root, text="Añadir Alumno", command=lambda: self.añadirAlumnoFuncion())
        self.añadirAlumnoBoton.grid(
            row=self.varFila, column=0, padx=10, pady=10)

        self.eliminarAlumnoBoton = Button(
            self.root, text="Eliminar Alumno", command=lambda: self.eliminarAlumnoFuncion())
        self.eliminarAlumnoBoton.grid(
            row=self.varFila, column=2, padx=10, pady=10)


miApp = App()
