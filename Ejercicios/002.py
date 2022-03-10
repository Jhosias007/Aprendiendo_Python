import tkinter as tk
from tkinter import StringVar, TclError, messagebox
import sqlite3


class App:
    # ? Variables
    varFila = 2

    # * Lo siguiente es para cargar los datos de la base a la app cuando se inicia
    listaDeClaves_id = list()
    listaDeClaves_nombre = list()
    listaDeClaves_nota = list()

    nombre_LabelId = "labelId"
    nombre_LabelNombre = "labelNombre"
    nombre_LabelNota = "labelNota"

    posicionDeLabel = 0
    contadorParaNombre_LabelId = 1

    # * Lo siguiente es para mostrar al nuevo alumno en app
    diccionario_ID = dict()
    diccionario_Nombre = dict()
    diccionario_Nota = dict()

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

    # * Funciones de boton añadir alumno
    def generarRootAñadirAlumno(self):
        self.rootAñadirAlumno = tk.Tk()
        self.rootAñadirAlumno.title("Añadir Alumno")

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
        try:
            self.listaNuevoAlumno = list()

            # * Conexion a base y creacion de cursor y tabla

            self.conexionDeBase = sqlite3.connect("Base_002.db")

            self.cursorDeBase = self.conexionDeBase.cursor()
            self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR (20),
                nota INTEGER
            )''')

            # * Agrego el nombre y la nota a la lista

            if self.entryNombre_AñadirAlumnoRoot.get().isalpha() == False:
                messagebox.showerror(
                    "Nombre", "El nombre ingresado solo debe contener caracteres alfabeticos")
                self.rootAñadirAlumno.mainloop()
            else:
                self.listaNuevoAlumno.append(
                    str(self.entryNombre_AñadirAlumnoRoot.get()))

            if self.entryNota_AñadirAlumnoRoot.get().isdigit() == False:
                messagebox.showerror(
                    "Nota", "Solo debes ingresar caracteres numericos en la nota")
                self.rootAñadirAlumno.mainloop()
            
            elif int(self.entryNota_AñadirAlumnoRoot.get()) < 0 or int(self.entryNota_AñadirAlumnoRoot.get()) > 20:
                messagebox.showerror("Nota", "El rango de nota es del 0 - 20")
                self.rootAñadirAlumno.mainloop()
            else:
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

        except TclError:
            pass

    def mostrarAlumnoAñadidoEnApp(self, id, nombre, nota):

        # * Obtengo el valor de varFila

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.varFila = int(len(self.cursorDeBase.fetchall())) + 2

        # * Agrego El ID
        self.diccionario_ID[self.nombre_LabelId +
                            str(id)] = tk.Label(self.root, text=id)

        self.diccionario_ID[self.nombre_LabelId +
                            str(id)].grid(row=self.varFila, column=0)

        # * Agrego Los Nombres
        self.diccionario_Nombre[self.nombre_LabelNombre + str(
            id)] = tk.Label(self.root, text=nombre)
        self.diccionario_Nombre[self.nombre_LabelNombre + str(
            id)].grid(row=self.varFila, column=1)

        # * Agrego Las Notas
        self.diccionario_Nota[self.nombre_LabelNota + str(
            id)] = tk.Label(self.root, text=nota)
        self.diccionario_Nota[self.nombre_LabelNota + str(
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
        tk.Label(self.rootEliminarAlumno, text="Eliminar Alumno").grid(
            row=0, column=0, columnspan=2, padx=7, pady=7)
        tk.Label(self.rootEliminarAlumno, text="ID del Alumno").grid(
            row=1, column=0, padx=7, pady=7)

        # * Entrys principales
        self.entryID_EliminarAlumnoRoot_SV = StringVar()
        self.entryID_EliminarAlumnoRoot = tk.Entry(
            self.rootEliminarAlumno, textvariable=self.entryID_EliminarAlumnoRoot_SV)
        self.entryID_EliminarAlumnoRoot.grid(row=1, column=1, padx=7, pady=7)

        # * Botones principales
        self.buttonEnviar_EliminarAlumnoRoot = tk.Button(
            self.rootEliminarAlumno, text="Enviar", command=lambda: self.eliminarAlumnoFuncion())
        self.buttonEnviar_EliminarAlumnoRoot.grid(
            row=2, column=0, columnspan=2, padx=7, pady=7)

        self.rootEliminarAlumno.mainloop()

    def eliminarAlumnoFuncion(self): # ! Corregir, cuando elimino un alumno con id de 2 digitos hay error

        self.conexionDeBase = sqlite3.connect("Base_002.db")

        self.cursorDeBase = self.conexionDeBase.cursor()
        self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (20),
            nota INTEGER
        )''')

        self.cursorDeBase.execute("SELECT id FROM alumnos")
        self.consultarIdsParaBorrarAl = str(
            self.cursorDeBase.fetchall()).replace("(", "").replace(",)", "")

        self.idDeAlumnoAEliminar = self.entryID_EliminarAlumnoRoot.get()

        if self.idDeAlumnoAEliminar in self.consultarIdsParaBorrarAl:
            self.cursorDeBase.execute(
                "DELETE FROM alumnos WHERE id=?", self.idDeAlumnoAEliminar)
            self.rootEliminarAlumno.destroy()
            messagebox.showinfo("Alumno Eliminado",
                                "Se ha eliminado el alumno correctamente")
        else:
            messagebox.showerror("ID Alumno", "El ID ingresado no existe")

        self.conexionDeBase.commit()

        self.quitarAlumnoDeApp(self.idDeAlumnoAEliminar)

    def quitarAlumnoDeApp(self, id):

        # * Elimino el alumno ingresado del diccionario de id
        if self.nombre_LabelId + str(id) in self.diccionario_ID.keys():
            self.diccionario_ID[self.nombre_LabelId + str(id)].destroy()
            del self.diccionario_ID[self.nombre_LabelId + str(id)]
        else:
            pass

        # * Elimino el alumno ingresado del diccionario de nombre
        if self.nombre_LabelNombre + str(id) in self.diccionario_Nombre.keys():
            self.diccionario_Nombre[self.nombre_LabelNombre +
                                    str(id)].destroy()
            del self.diccionario_Nombre[self.nombre_LabelNombre + str(id)]
        else:
            pass

        # * Elimino el alumno ingresado del diccionario de nota
        if self.nombre_LabelNota + str(id) in self.diccionario_Nota.keys():
            self.diccionario_Nota[self.nombre_LabelNota + str(id)].destroy()
            del self.diccionario_Nota[self.nombre_LabelNota + str(id)]
        else:
            pass

    # * ---------------------------------- Funciones de Menu --------------------------------------------

    # * Funciones de menu Alumnos

    def funcionNuevaVentana_MenuAlumnos(self):
        pass  # ! crear nueva ventana al llamar la funcion

    def funcionSalir_MenuAlumnos(self):
        self.varSalir = messagebox.askokcancel(
            "Salir", "¿Deseas salir de la aplicacion?")

        if self.varSalir == True:
            self.root.destroy()

    # * Funciones de menu Archivo

    def funcionEditarAlumno_MenuArchivo(self):
        self.rootEditarAlumno_1 = tk.Tk()
        self.rootEditarAlumno_1.title("Editar Alumno")

        # * Labels Principales
        tk.Label(self.rootEditarAlumno_1, text="Editar Alumno").grid(
            row=0, column=0, columnspan=2, padx=7, pady=7)
        tk.Label(self.rootEditarAlumno_1, text="ID del Alumno").grid(
            row=1, column=0, padx=7, pady=7)

        # * Entrys Principales
        self.entryId_EditarAlumnoRoot_SV = StringVar()
        self.entryId_EditarAlumnoRoot = tk.Entry(
            self.rootEditarAlumno_1, textvariable=self.entryId_EditarAlumnoRoot_SV)
        self.entryId_EditarAlumnoRoot.grid(row=1, column=1, padx=7, pady=7)

        # * Botones Principales
        self.botonContinuar_EditarAlumnoRoot = tk.Button(
            self.rootEditarAlumno_1, text="Enviar", command=lambda: self.generarRootEditarAlumno())
        self.botonContinuar_EditarAlumnoRoot.grid(
            row=2, column=0, columnspan=2, padx=7, pady=7)

        self.rootEditarAlumno_1.mainloop()

        self.generarRootEditarAlumno()

    def generarRootEditarAlumno(self):
        try:
            self.idDeAlumnoAEditar = self.entryId_EditarAlumnoRoot.get()

            # * Obtengo los datos de id
            self.conexionDeBase = sqlite3.connect("Base_002.db")
            self.cursorDeBase = self.conexionDeBase.cursor()
            self.cursorDeBase.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR (20),
                nota INTEGER
            )''')

            self.cursorDeBase.execute("SELECT id FROM alumnos")
            self.listaDeIdParaVerificarEdicion = str(self.cursorDeBase.fetchall()).replace(
                "(", "").replace(")", "").replace(",", "")

            # * Confirmo que el ID sea un numero
            if self.idDeAlumnoAEditar.isdigit() == False:
                messagebox.showerror("ID", "El ID ingresado no es valido")
                self.rootEditarAlumno_1.mainloop()

            # * Confirmo que el id se encuentre en la base
            if self.idDeAlumnoAEditar not in self.listaDeIdParaVerificarEdicion:
                messagebox.showerror("ID Alumno", "El ID ingresado no existe")

            else:
                self.rootEditarAlumno_1.destroy()

                self.rootEditarAlumno_2 = tk.Tk()
                self.rootEditarAlumno_2.title("Editar Alumno")

                # * Labels Principales
                tk.Label(self.rootEditarAlumno_2, text="Editar Alumno").grid(
                    row=0, column=0, columnspan=2, padx=7, pady=7)
                tk.Label(self.rootEditarAlumno_2, text="Nombre").grid(
                    row=1, column=0, padx=7, pady=7)
                tk.Label(self.rootEditarAlumno_2, text="Nota").grid(
                    row=2, column=0, padx=7, pady=7)

                # * Entrys Principales
                self.entryNombre_EditarAlumnoRoot2 = tk.Entry(
                    self.rootEditarAlumno_2)
                self.entryNombre_EditarAlumnoRoot2.grid(
                    row=1, column=1, padx=7, pady=7)

                self.entryNota_EditarAlumnoRoot2 = tk.Entry(
                    self.rootEditarAlumno_2)
                self.entryNota_EditarAlumnoRoot2.grid(
                    row=2, column=1, padx=7, pady=7)

                # * Buttons Principales
                self.botonGuardar_AñadirAlumnoRoot2 = tk.Button(
                    self.rootEditarAlumno_2, text="Guardar", command=lambda: self.funcionGuardarCambios_EditarAlumnoRoot2())
                self.botonGuardar_AñadirAlumnoRoot2.grid(
                    row=3, column=0, columnspan=2, padx=7, pady=7)

                self.rootEditarAlumno_2.mainloop()

        except TclError:
            pass

    def funcionGuardarCambios_EditarAlumnoRoot2(self):
        # * Declaro variables (vars de nombre y nota que remplazaran)

        if self.entryNombre_EditarAlumnoRoot2.get().isalpha() == False:
            messagebox.showerror(
                "Nombre", "Solo debes ingresar caracteres alfabeticos en el nombre")
            self.rootEditarAlumno_2.mainloop()
        else:
            self.nombreAEditar = self.entryNombre_EditarAlumnoRoot2.get()

        if self.entryNota_EditarAlumnoRoot2.get().isdigit() == False:
            messagebox.showerror(
                "Nota", "Solo debes ingresar caracteres numericos en la nota")
            self.rootEditarAlumno_2.mainloop()
        else:
            self.notaAEditar = self.entryNota_EditarAlumnoRoot2.get()

        # * Agrego el nombre y el id a la lista
        self.listaDeDatosNombre_ActualizarAlumno = [
            str(self.nombreAEditar), int(self.idDeAlumnoAEditar)]

        # * Agrego la nota y el id a la lista
        self.listaDeDatosNota_ActualizarAlumno = [
            str(self.notaAEditar), int(self.idDeAlumnoAEditar)]

        # * Realizo los cambios de nombre y nota en la base
        self.cursorDeBase.execute("UPDATE alumnos SET nombre=? WHERE id=?", self.listaDeDatosNombre_ActualizarAlumno)
        self.cursorDeBase.execute("UPDATE alumnos SET nota=? WHERE id=?", self.listaDeDatosNota_ActualizarAlumno)

        self.conexionDeBase.commit()

        self.rootEditarAlumno_2.destroy()

        messagebox.showinfo("Alumno", "La informacion del alumno ha sido actualizada correctamente")

    def funcionVerAprobados_MenuArchivo(self):
        pass

    def funcionVerDesaprobados_MenuArchivo(self):
        pass

    # * Funciones de menu Ayuda

    def funcionLicencia_MenuAyuda(self):
        messagebox.showinfo("Licencia", "La licencia es mia")

    def funcionAcercaDe_MenuAyuda(self):
        messagebox.showinfo(
            "Acerca De", "App creada desde el 02 de marzo de 2022 al \n xx de blablabla")

    # * Funciones para generar GUI completo
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
            self.diccionario_ID[self.nombre_LabelId + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_id[self.posicionDeLabel])
            self.diccionario_ID[self.nombre_LabelId + str(
                self.contadorParaNombre_LabelId)].grid(row=self.varFila, column=0)

            self.varFila += 1
            self.contadorParaNombre_LabelId += 1
            self.posicionDeLabel += 1

        self.contadorParaNombre_LabelId = 1
        self.posicionDeLabel = 0
        self.varFila = 2

        # * Creo los labels de Nombre
        for i in self.listaDeClaves_nombre:
            self.diccionario_Nombre[self.nombre_LabelNombre + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_nombre[self.posicionDeLabel])
            self.diccionario_Nombre[self.nombre_LabelNombre + str(
                self.contadorParaNombre_LabelId)].grid(row=self.varFila, column=1)

            self.varFila += 1
            self.contadorParaNombre_LabelId += 1
            self.posicionDeLabel += 1

        self.contadorParaNombre_LabelId = 1
        self.posicionDeLabel = 0
        self.varFila = 2

        # * Creo los labels de Nota
        for i in self.listaDeClaves_nota:
            self.diccionario_Nota[self.nombre_LabelNota + str(self.contadorParaNombre_LabelId)] = tk.Label(
                self.root, text=self.listaDeClaves_nota[self.posicionDeLabel])
            self.diccionario_Nota[self.nombre_LabelNota + str(
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
        self.menuArchivo.add_command(
            label="Nueva Ventana", command=lambda: self.funcionNuevaVentana_MenuAlumnos())
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(
            label="Salir", command=lambda: self.funcionSalir_MenuAlumnos())

        # Opciones del sub menu "menuAlumnos"
        self.menuAlumnos.add_command(
            label="Añadir Alumno", command=lambda: self.generarRootAñadirAlumno())
        self.menuAlumnos.add_command(
            label="Eliminar Alumno", command=lambda: self.generarRootEliminarAlumno())
        self.menuAlumnos.add_command(
            label="Editar Alumno", command=lambda: self.funcionEditarAlumno_MenuArchivo())
        self.menuAlumnos.add_separator()
        self.menuAlumnos.add_command(
            label="Ver Aprobados", command=lambda: self.funcionVerAprobados_MenuArchivo())
        self.menuAlumnos.add_command(
            label="Ver Desaprobados", command=lambda: self.funcionVerDesaprobados_MenuArchivo())

        # Opciones del sub menu "menuAyuda"
        self.menuAyuda.add_command(
            label="Licencia", command=lambda: self.funcionLicencia_MenuAyuda())
        self.menuAyuda.add_command(
            label="Acerca De", command=lambda: self.funcionAcercaDe_MenuAyuda())

        # * Hago visible el menu principal y los sub menus
        self.menuPrincipal.add_cascade(menu=self.menuArchivo, label="Alumnos")
        self.menuPrincipal.add_cascade(menu=self.menuAlumnos, label="Archivo")
        self.menuPrincipal.add_cascade(menu=self.menuAyuda, label="Ayuda")


app_001 = App()

# ! Dia 2 de Marzo del 2022. Comienza Epicamente*
# ! Logre que los labels se eliminen en tiempo real :))))))) (Hoy es 08 de marzo del 2022)
