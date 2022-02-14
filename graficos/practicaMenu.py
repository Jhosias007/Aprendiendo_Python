from tkinter import *
from tkinter import messagebox

root = Tk()

# funciones


def infoAdicional():
    messagebox.showinfo("Procesador de Andre", "Procesador de textos 2022")


def avisoLisencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia de mi")


def salirApp():
    #varSalir = messagebox.askquestion("Salir?, para que?", "Deseas salir de la aplicacion(dale a no)")
    varSalir = messagebox.askokcancel(
        "Salir?, para que?", "Deseas salir de la aplicacion(dale a no)")

    if varSalir == True:
        root.destroy()


def cerrarDocumento():
    varSalir = messagebox.askretrycancel(
        "Reintentar", "No es posible cerrar. Documento Bloqueado")


# Creacion Menu
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Partes Menu
archivoMenu = Menu(barraMenu, tearoff=False)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirApp)


archivoEdicion = Menu(barraMenu, tearoff=False)
archivoEdicion.add_command(label="Copiar - Ctrl+C")
archivoEdicion.add_command(label="Pegar - Ctrl+V")
archivoEdicion.add_command(label="Cortar - Ctrl+X")


archivoHerramientas = Menu(barraMenu, tearoff=False)


archivoAyuda = Menu(barraMenu, tearoff=False)
archivoAyuda.add_command(label="Licencia", command=avisoLisencia)
archivoAyuda.add_command(label="Acerca De", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()

"""
Menu():
    Menu() es una clase que nos permite crear objetos en los cuales podamos acceder a ellos
    Sintaxis:
        nuevoMenu = Menu(root)
    
    Cuando creas un Menu tienes que hacerlo notar a tu frame con el metodo .config(). Ej:
        root.config(menu=nuevoMenu)

    Una vez creado tu Menu tienes que crear los ESPACIOS DEL MENU (como suelen ser: Archivo, Editar, Ayuda, etc)
    Esto lo consigues de la misma forma de la que creas un Menu pero ahora le indicas que este pertenece
    al menu principal. Ej:
        archivoMenu = Menu(nuevoMenu)
    
    Luego puedes añadir subMenus con el metodo .add_command(). Ej:
        archivoMenu.add_command(label="Nuevo Archivo")
    Nota: En ves de colocar text="" para indicar el texto se coloca label=""

    Para que todo esto sea visible tienes que colocar el metodo .add_cascade() a el menu Principal. Ej:
        nuevoMenu.add_cascade(label="Archivo", menu=archivoMenu)

    Codigo Entero:
    
        from tkinter import *
        
        root = Tk()
        nuevoMenu = Menu(root)
        root.config(menu=nuevoMenu)

        archivoMenu = Menu(nuevoMenu)
        archivoMenu.add_command(label="Nuevo Archivo")
        nuevoMenu.add_cascade(label="Archivo", menu=archivoMenu)
"""