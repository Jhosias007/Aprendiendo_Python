from tkinter import *
import sqlite3


class App():
    def __init__(self):
        # ? Crear root
        self.root = Tk()
        self.root.title("Alumnos")

        # ? Funciones llamadas
        self.generarMenu()
        self.generarPlantilla(1)
        self.root.mainloop()

        # ? Conexion a SQLite3
        self.conexion = sqlite3.connect("Base.db")
        self.cursor = self.conexion.cursor()

    def crearTabla(self):
        self.cursor.execute(
            "CREATE TABLE ALUMNOS (NOMBRE VARCHAR (50), NOTA INTEGER)")

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
        self.entryNombreAñadirAlumno = Entry(self.rootAñadirAlumno)
        self.entryNombreAñadirAlumno.grid(row=1, column=1, padx=10, pady=10)

        self.stringVarNotaAñadirAlumno = StringVar()
        self.entryNotaAñadirAlumno = Entry(self.rootAñadirAlumno)
        self.entryNotaAñadirAlumno.grid(row=2, column=1, padx=10, pady=10)

        self.buttonEnviarAñadirAlumno = Button(
            self.rootAñadirAlumno, text="Guardar Alumno", command=lambda: self.capturarDatosAñadirAlumno())
        self.buttonEnviarAñadirAlumno.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

        self.rootAñadirAlumno.mainloop()
        self.cursor.execute(
            "INSERT INTO ALUMNOS VALUES (?, ?)", self.infoAlumnos)

    def capturarDatosAñadirAlumno(self):
        self.infoAlumnoAñadir = (
            self.stringVarNombreAñadirAlumno.get(), self.stringVarNotaAñadirAlumno.get())

        self.cursor.execute("INSERT INTO ALUMNOS VALUES (?, ?)", self.infoAlumnoAñadir)

        self.rootAñadirAlumno.destroy()

    def eliminarAlumnoFuncion(self):
        pass

    def generarMenu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.archivo = Menu(self.menu, tearoff=False)
        self.archivo.add_command(label="Conectarse")
        self.archivo.add_separator()
        self.archivo.add_command(label="Salir")

        self.alumnos = Menu(self.menu, tearoff=False)
        self.alumnos.add_command(label="Agregar Alumno")
        self.alumnos.add_command(label="Eliminar Alumno")
        self.alumnos.add_separator()
        self.alumnos.add_command(label="Ver Aprobados")
        self.alumnos.add_command(label="Ver Desaprobados")

        self.ayuda = Menu(self.menu, tearoff=False)
        self.ayuda.add_command(label="Licencia")
        self.ayuda.add_command(label="Acerca De")

        self.menu.add_cascade(menu=self.archivo, label="Archivo")
        self.menu.add_cascade(menu=self.alumnos, label="Alumnos")
        self.menu.add_cascade(menu=self.ayuda, label="Ayuda")

    def generarPlantilla(self, cantAlumnos: int):

        # * Labels
        self.cantAlumnos = cantAlumnos
        self.labelTitulo = Label(self.root, text="ALUMNOS")
        self.labelTitulo.grid(row=0, column=1)

        self.varFila = 1

        for i in range(self.cantAlumnos):
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

        self.añadirAlumno = Button(
            self.root, text="Añadir Alumno", command=lambda: self.añadirAlumnoFuncion())
        self.añadirAlumno.grid(row=self.varFila, column=0, padx=10, pady=10)

        self.eliminarAlumno = Button(
            self.root, text="Eliminar Alumno", command=lambda: self.eliminarAlumnoFuncion())
        self.eliminarAlumno.grid(row=self.varFila, column=2, padx=10, pady=10)


miApp = App()
