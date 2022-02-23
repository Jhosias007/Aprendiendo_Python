from tkinter import *
import sqlite3


class App():
    def __init__(self):
        # ? Crear root
        self.root = Tk()
        self.root.title("Alumnos")

        # ? Funciones llamadas
        self.generarMenu()
        self.generarPlantilla(3)
        self.root.mainloop()

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
            self.root, text="Añadir Alumno", command=lambda: self.funcionAñadirAlumno())
        self.añadirAlumno.grid(row=self.varFila, column=0, padx=10, pady=10)

        self.eliminarAlumno = Button(
            self.root, text="Eliminar Alumno", command=lambda: self.funcionEliminarAlumno())
        self.eliminarAlumno.grid(row=self.varFila, column=2, padx=10, pady=10)

    def funcionAñadirAlumno(self):
        self.cantAlumnos += 1

    def funcionEliminarAlumno(self):
        pass


miApp = App()
