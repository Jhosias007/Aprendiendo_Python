from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import sqlite3

# ---------- Funciones -----------------------------------------------------------------------------------

# Menu - Funciones ---------------------------------------------------------------------------------------

# BBDD - Menu - Funciones --------------------------------------------------------------------------------

conexionBaseDatos = sqlite3.connect("CRUD.db")
cursor = conexionBaseDatos.cursor()


def conectarseFuncion():
    try:
        cursor.execute('''CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(10),
            PASSWORD VARCHAR(8),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(40),
            COMENTARIO VARCHAR(200)
        )''')
        messagebox.showinfo(
            "Conexion", "Te has conectado a la base de datos exitosamente")
    except sqlite3.OperationalError:
        messagebox.showinfo(
            "Conexion", "Ya estas conectado a la Base de Datos")


def salirFuncion():
    resultadoSalir = messagebox.askyesno(
        "Salir", "¿Deseas salir de la aplicacion?")
    if resultadoSalir == YES:
        root.destroy()


# Borrar - Menu - Funciones -------------------------------------------------------------------------------

def borrarFuncion():
    idStringVar.set("")
    nombreStringVar.set("")
    passwordStringVar.set("")
    apellidoStringVar.set("")
    direccionStringVar.set("")
    comentarioEntry.delete("1.0", "end")


# CRUD - Menu - Funciones ---------------------------------------------------------------------------------

def crearFuncion():
    try:
        if idStringVar.get() == "":
            conjuntoInfo = (
                str(nombreStringVar.get()),
                str(passwordStringVar.get()),
                str(apellidoStringVar.get()),
                str(direccionStringVar.get()),
                str(comentarioEntry.get("1.0", "end"))
            )

            cursor.execute('''
                INSERT INTO DATOS_USUARIOS (ID, NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION, COMENTARIO) 
                VALUES (NULL, ?, ?, ?, ?, ?)''', conjuntoInfo
                           )

            messagebox.showinfo("Datos", "Se han cargado los datos en la base")

        else:
            conjuntoInfo = (
                int(idStringVar.get()),
                str(nombreStringVar.get()),
                str(passwordStringVar.get()),
                str(apellidoStringVar.get()),
                str(direccionStringVar.get()),
                str(comentarioEntry.get("1.0", "end"))
            )

            cursor.execute('''
            INSERT INTO DATOS_USUARIOS (ID, NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION, COMENTARIO) 
            VALUES (?, ?, ?, ?, ?, ?)''', conjuntoInfo
                           )

            messagebox.showinfo("Datos", "Se han cargado los datos en la base")

        conexionBaseDatos.commit()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "ID Existente", "El ID ingresado ya esta ocupado, ingresa otro")


def leerFuncion():
    if idStringVar.get() == "":
        messagebox.showerror("BBDD", "Debes colocar un ID para leer sus datos")

    else:
        registroALeer = (int(idStringVar.get()), )
        cursor.execute(
            "SELECT ID FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        idStringVar.set(leerVariable)

        cursor.execute(
            "SELECT NOMBRE_USUARIO FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        nombreStringVar.set(leerVariable)

        cursor.execute(
            "SELECT PASSWORD FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        passwordStringVar.set(leerVariable)

        cursor.execute(
            "SELECT APELLIDO FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        apellidoStringVar.set(leerVariable)

        cursor.execute(
            "SELECT DIRECCION FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        direccionStringVar.set(leerVariable)

        cursor.execute(
            "SELECT COMENTARIO FROM DATOS_USUARIOS WHERE ID=?", registroALeer)
        leerVariable = cursor.fetchall()
        comentarioEntry.insert("1.0", leerVariable)


def actualizarFuncion():
    if idStringVar.get() == "":
        messagebox.showerror(
            "BBDD", "Debes colocar un ID para actualizar sus datos")

    else:
        nombreAActualizar = (str(nombreStringVar.get()),
                             int(idStringVar.get()))
        if nombreStringVar.get() != "":
            cursor.execute(
                "UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=? WHERE ID=?", nombreAActualizar)

        passwordAActualizar = (str(passwordStringVar.get()),
                               int(idStringVar.get()))
        if passwordStringVar.get() != "":
            cursor.execute(
                "UPDATE DATOS_USUARIOS SET PASSWORD=? WHERE ID=?", passwordAActualizar)

        apellidoAActualizar = (str(apellidoStringVar.get()),
                               int(idStringVar.get()))
        if apellidoStringVar.get() != "":
            cursor.execute(
                "UPDATE DATOS_USUARIOS SET APELLIDO=? WHERE ID=?", apellidoAActualizar)

        direccionAActualizar = (
            str(direccionStringVar.get()), int(idStringVar.get()))
        if direccionStringVar.get() != "":
            cursor.execute(
                "UPDATE DATOS_USUARIOS SET DIRECCION=? WHERE ID=?", direccionAActualizar)

        comentarioAActualizar = (
            str(comentarioEntry.get("1.0", "end")), int(idStringVar.get()))
        if comentarioEntry.get("1.0", "end") != "":
            cursor.execute(
                "UPDATE DATOS_USUARIOS SET COMENTARIO=? WHERE ID=?", comentarioAActualizar)

        conexionBaseDatos.commit()
        messagebox.showinfo(
            "BBDD", "Se han actualizado los datos correctamente")


def eliminarFuncion():
    idEliminar = (int(idStringVar.get()), )
    cursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=?", idEliminar)
    messagebox.showinfo(
        "BBDD", "Se ha eliminado el el registro con ID: " + idStringVar.get() + " de la base")
    conexionBaseDatos.commit()


# Ayuda - Menu - Funciones --------------------------------------------------------------------------------

def funcionLicencia():
    messagebox.showinfo("Licencia", "La licencia es mia, XD")


def funcionAcercaDe():
    messagebox.showinfo("Acerca De", "Programa hecho por mi en este año")


# ---------- Interfaz Grafica -----------------------------------------------------------------------------

# Root - Interfaz Grafica ---------------------------------------------------------------------------------


root = Tk()
root.title("CRUD Intento 1")

# Menu - Interfaz Grafica ---------------------------------------------------------------------------------

menu = Menu(root)
root.config(menu=menu, width=300, height=400)
root.resizable(False, False)

bbddMenu = Menu(menu, tearoff=False)
bbddMenu.add_command(label="Conectarse", command=lambda: conectarseFuncion())
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salirFuncion)

borrar = Menu(menu, tearoff=False)
borrar.add_command(label="Borrar Todo", command=borrarFuncion)

crudMenu = Menu(menu, tearoff=False)
crudMenu.add_command(label="Crear", command=lambda: crearFuncion())
crudMenu.add_command(label="Leer", command=lambda: leerFuncion())
crudMenu.add_command(label="Actualizar", command=lambda: actualizarFuncion())
crudMenu.add_command(label="Eliminar", command=lambda: eliminarFuncion())

ayuda = Menu(menu, tearoff=False)
ayuda.add_command(label="Licencia", command=lambda: funcionLicencia())
ayuda.add_command(label="Acerca De", command=lambda: funcionAcercaDe())

menu.add_cascade(menu=bbddMenu, label="BBDD")
menu.add_cascade(menu=borrar, label="Borrar")
menu.add_cascade(menu=crudMenu, label="CRUD")
menu.add_cascade(menu=ayuda, label="Ayuda")

# Labels - Interfaz Grafica -------------------------------------------------------------------------------

idLabel = Label(root, text="ID: ")
idLabel.grid(row=1, column=2, padx=10, pady=10)

nombreLabel = Label(root, text="Nombre: ")
nombreLabel.grid(row=2, column=2, padx=10, pady=10)

passwordLabel = Label(root, text="Password: ")
passwordLabel.grid(row=3, column=2, padx=10, pady=10)

apellidoLabel = Label(root, text="Apellido: ")
apellidoLabel.grid(row=4, column=2, padx=10, pady=10)

direccionLabel = Label(root, text="Direccion: ")
direccionLabel.grid(row=5, column=2, padx=10, pady=10)

comentariosLabel = Label(root, text="Comentarios: ")
comentariosLabel.grid(row=6, column=2, padx=10, pady=10)

# Entry's - Interfaz Grafica ------------------------------------------------------------------------------

idStringVar = StringVar()
idEntry = Entry(root, textvariable=idStringVar)
idEntry.grid(row=1, column=3, padx=10, pady=10)

nombreStringVar = StringVar()
nombreEntry = Entry(root, textvariable=nombreStringVar)
nombreEntry.grid(row=2, column=3, padx=10, pady=10)

passwordStringVar = StringVar()
passwordEntry = Entry(root, textvariable=passwordStringVar, show="*")
passwordEntry.grid(row=3, column=3, padx=10, pady=10)

apellidoStringVar = StringVar()
apellidoEntry = Entry(root, textvariable=apellidoStringVar)
apellidoEntry.grid(row=4, column=3, padx=10, pady=10)

direccionStringVar = StringVar()
direccionEntry = Entry(root, textvariable=direccionStringVar)
direccionEntry.grid(row=5, column=3, padx=10, pady=10)

comentarioEntry = scrolledtext.ScrolledText(
    root, width=14, height=7, wrap="word")
comentarioEntry.grid(row=6, column=3, padx=10, pady=10)

# Buttons - Interfaz Grafica ------------------------------------------------------------------------------

createButton = Button(root, text="Create", command=lambda: crearFuncion())
createButton.grid(row=7, column=1, padx=10, pady=10)

readButton = Button(root, text="Read", command=lambda: leerFuncion())
readButton.grid(row=7, column=2, padx=10, pady=10)

updateButton = Button(root, text="Update", command=lambda: actualizarFuncion())
updateButton.grid(row=7, column=3, padx=10, pady=10)

deleteButton = Button(root, text="Delete", command=lambda: eliminarFuncion())
deleteButton.grid(row=7, column=4, padx=10, pady=10)

conexionBaseDatos.commit()

root.mainloop()
