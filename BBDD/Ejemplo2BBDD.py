import sqlite3

conexion = sqlite3.connect("GestionProductos")
cursor = conexion.cursor()

# CRUD - C - CREATE

cursor.execute('''CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR (50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR (20))''')

productosLista = [
    ("pelota", 15, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("pantalones", 35, "confeccion"),
    ("destonrillador", 25, "ferreteria"),
    ("jarron", 45, "cerámica")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productosLista)
cursor.execute(
    "INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")


# CURD - R - READ
"""
cursor.execute("SELECT * FROM PRODUCTOS WHERE ID=2")
readCRUD = cursor.fetchall()
for i in readCRUD:
    print(i)
"""


# CRUD - U - UPDATE
"""
cursor.execute(
    "UPDATE PRODUCTOS SET PRECIO='35' WHERE NOMBRE_ARTICULO='pelota'")
"""


# CRUD - D - DELETE
"""
cursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
"""


conexion.commit()
conexion.close()
# 46


"""
Campo Clave:
    Un "Campo Clave" es un campo que identificará cada registo o cada producto de una tabla (Es como un ID)
    Podemos hacer que el codigo vaya generando un campo clave a cada uno de los articulos creados o añadidos
    a la base. Esto lo hacemos al crear una tabla de la siguiente forma:
        
        (ID INTEGER PRIMARY KEY AUTOINCREMENT)

        Esta parte del codigo pertenece a un encabezado de una tabla que estamos creando
        La palabra "ID" le indica que se creara un encabezado de nombre ID
        La palabra "INTEGER" indica que sera de tipo entero / int
        Las palabras "PRIMARY KEY" indican que lo que se almacene en este campo sera unico para cada "objeto"
            y que no se podran repetir con otros
        La palabra "AUTOINCREMENT" indica que a medida que se vayan rellenando de informacion en este
            campo, el valor de "ID" se irá incrementando tambien

        Podemos ver esta linea de codigo como si fuera una variable que se le va sumando 1 cada ves que
            entre nueva informacion de "objetos".

# CRUD - C - CREATE
    Explicado en el archivo: "Ejemplo1BBDD.py"

# CURD - R - READ
    Para leer los "objetos" o informacion almacenada en la base debemos usar el metodo .execute() en el
    puntero y luego capturar la informacion extraida dela base en una variable con el metodo .fetchall(). Ej:
        cursor.execute("SELECT * FROM PRODUCTOS WHERE ID=2")
        readCRUD = cursor.fetchall()
    Con "SELECT * FROM PRODUCTOS" indicamos que vamos a extraer todo(*) lo que haiga en la tabla PRODUCTOS
    Con "WHERE ID=2" indicamos que de la tabla vamos a extraer lo que se encuentre en el encabezado, en 
    este caso el ID, y por ende, tendremos que seleccionar pedirle un ID especifico.
    Tambien podemos pedirle otro encabezade despues de WHERE, como el NOMBRE_ARTICULO o SECCION, siempre
    y cuando se indique lo que se busca en este encabezado (es decir, siempre que le pasemos un parametro)

    Podemos pedirle que nos lea toda la base quitando el WHERE... y tambien podemos hacer que nos lea
    indicandole otro encabezado como "NOMBRE_ARTICULO"

# CRUD - U - UPDATE
    Para actualizar la tabla debemos hacer uso del metodo .execute() en el cursor. Ej:
        cursor.execute(
            "UPDATE PRODUCTOS SET PRECIO='35' WHERE NOMBRE_ARTICULO='pelota'")

    Con "UPDATE PRODUCTOS" le indicamos que tenemos que actualizar algo de la tabla PRODUCTOS en este caso
    Con "SET PRECIO=35" le indicamos que debe colocar(SET) en el encabezado(PRECIO) el valor 35(=35)
    Con "WHERE NOMBRE_ARTICULO='pelota'" le indicamos que debe hacer esta actualizacion de datos en(WHERE)
        el encabezado(NOMBRE_ARTICULO) y mas especificamente en el lugar que ocupe "pelota"
    
    Podemos cambiar lo que se desea actualizar con el SET, y tambien que es lo que se desea actualizar con el WHERE

# CRUD - D - DELETE
    Para eliminar algunos elementos de la base de datos debemos utilizar el metodo .execute() en el cursor
    Ej. 
        cursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
    Para eliminar directamente todo el contenido la base podemos poner directamente "DELETE FORM PRODUCTOS"
    Pero para eliminar algo mas especifico hacemos uso de "WHERE", le indicamos el encabezado y le indicamos
    cual es el contenido dentro del encabezado que borrará

    Si hay 2 o mas "objetos" ocupando el mismo encabezado se borraran todos estos.
    Podemos indicarle otro encabezado y otro objeto que borrara cambiando lo que hay acontinuacion del "WHERE"


"""
