from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import sqlite3
import os

#  ---------- Funciones -----------------------------------------------------------------------------------

# Menu - Funciones ----------------------------------------------------------------------------------------

# BBDD - Menu - Funciones ---------------------------------------------------------------------------------


def conectarseFuncion():
    global cursor
    global coneccionBaseDatos
    try:
        coneccionBaseDatos = sqlite3.connect("CRUD")      
        cursor = coneccionBaseDatos.cursor()
        cursor.execute('''CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(10),
            PASSWORD VARCHAR(8),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(40),
            COMENTARIO VARCHAR(200)
        )''')
        messagebox.showinfo(
            "Coneccion", "Te has conectado a la base de datos exitosamente")
    except sqlite3.OperationalError:
        messagebox.showinfo(
            "Coneccion", "Ya estas conectado a la Base de Datos")


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
    global coneccionBaseDatos
    global cursor
    coneccionBaseDatos = sqlite3.connect("CRUD")
    cursor = coneccionBaseDatos.cursor()
    insertarDatos = [(nombreStringVar.get(), passwordStringVar.get(), apellidoStringVar.get(),
                      direccionStringVar.get(), comentarioEntry.get("1.0", "end"))]
    cursor.executemany(
        "INSERT INTO DATOS_USUARIOS VALUES (NULL, ?,?,?,?,?)", insertarDatos)
    messagebox.showinfo("CRUD", "Registro incertado con exito")


def leerFuncion():
    pass


def actualizarFuncion():
    pass


def eliminarFuncion():
    pass


# ---------- Interfaz Grafica -----------------------------------------------------------------------------

# Root - Interfaz Grafica ---------------------------------------------------------------------------------

root = Tk()
root.title("CRUD Intento 1")

# Menu - Interfaz Grafica ---------------------------------------------------------------------------------

menu = Menu(root)
root.config(menu=menu, width=300, height=400)

bbddMenu = Menu(menu, tearoff=False)
bbddMenu.add_command(label="Conectarse", command=conectarseFuncion)
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salirFuncion)

borrar = Menu(menu, tearoff=False)
borrar.add_command(label="Borrar Todo", command=borrarFuncion)

crudMenu = Menu(menu, tearoff=False)
crudMenu.add_command(label="Crear", command=crearFuncion)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Eliminar")

ayuda = Menu(menu, tearoff=False)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca De")

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

#frame = Frame(root, width=350, height=400)
# frame.pack()

createButton = Button(root, text="Create", command=crearFuncion)
createButton.grid(row=7, column=1, padx=10, pady=10)

readButton = Button(root, text="Read")
readButton.grid(row=7, column=2, padx=10, pady=10)

updateButton = Button(root, text="Update")
updateButton.grid(row=7, column=3, padx=10, pady=10)

deleteButton = Button(root, text="Delete")
deleteButton.grid(row=7, column=4, padx=10, pady=10)


root.mainloop()
