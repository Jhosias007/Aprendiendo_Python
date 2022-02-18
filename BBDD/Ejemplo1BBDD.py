import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', 15, 'DEPORTES')")


# Para agregar varios objetos a la base de datos podemos hacerlo con una lista que tenga tuplas en su interior
"""
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
"""

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for productos in variosProductos:
    print("Nombre Del Articulo: ",
          productos[0], " || ", "Seleccion: ", productos[2])

miConexion.commit()

miConexion.close()
#https://www.youtube.com/watch?v=HVd6mPiD3pc&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=57
#57

#MUCHA INFOOOOOOOOOOOOOOOO AAAAAAAAAAAAAAA

"""
sqlite3:
    sqlite3 es una libreria de python que se utiliza para hacer conexiones con una base de datos.
    Cuando creamos una conexion lo que hacemos es traer la base de datos a nuestra computadora y podemos
    visualizar su contenido con el programa "DB Browser SQLite".
    
    Para crear una conexion podemos usar el metodo .connect() de la libreria sqlite3. Ej:
        nuevaConexion = sqlite3.connect("NombreBaseDatos")
    Este recibe como parametro el nombre del archivo / base de datos al que se conectara entre comillas

    Para crear una tabla / CRUD, debemos crear un puntero/cursor en donde se almacenaran estos datos. 
    Para hacerlo tendremos que declarar el cursor e igualarlo a el nombre que se le dio la conexion creada
    en un principio junto con el metodo .cursor()   . Ej:
        nuevoCursor = nuevaConexion.cursor()

    Ahora con el cursor podemos usar metodos como el .execute() para crear una tabla. Ej:
        nuevoCursor.execute("CREATE TABLE PRODUCTOS (
            NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

    Lo que le pasamos por parametros al metodo .execute para crear la tabla (tiene que estar entre comillas):
        "CREATE TABLE NOMBRE_TABLA(...)" 
        Las palabras "CREATE TABLE" son fijas, obviamente es para indicar que crearemos una tabla
        La palabra "NOMBRE_TABLA" es simplemente un nombre cualquiera que le damos a la tabla que estamos creando
        
        A partir de los parentesis ponemos los datos que luego se ocuparan por los objetos que entren a la base
            (NOMBRE_ARTICULO VARCHAR(50))
            La primera palabra "NOMBRE_ARTICULO" es para indicar el encabezado de la informacion que ocupara
            cuando se rellene la tabla, por ejemplo, podremos decirle que eso sera igual a: "Silla".
            La palabra "VARCHAR(50)" indica el tipo de variable que se almacenara cuando se rellene al tabla
            No se lo que es este: (50), pero supongo que es para indicar un limite de caracteres

            (PRECIO INTEGER)
            Es lo mismo, la primera palabra indica una caracteristica que tendra la informacion al ser rellenada,
            en este caso seria una cantidad en numeros ya que le estamos indicando con la segunda palabra
            que este almacenara datos de tipo INTEGER (int/entero).
            Tampoco se porque no lleva unos parentesis como el caso anterior

            Podemos poner las caracteristicas que queramos que se le asignaran a la informacion que llegue a la base
            
    Luego de esto podremos empezar a llenar la base de datos desde el puntero con el mismo metodo .execute()
    Ej:
        nuevoCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', 15, 'DEPORTES')")

    Lo que pasamos por parametros para agregar informacion a la base:
        Las palabras "INSERT INTO" quieren decir que vamos a incertar informacion a la base de datos que le indiquemos
        La palabra "PRODUCTOS" es el nombre que le dimos a la base de datos, aqui se guardara la informacion
        La palabra "VALUES" es como la continuacion del codigo, que nos indica que insertaremos informacion/valores

        Lo que le pasamos en los siguientes parentesis indican la informacion de un objeto u otra cosa
        que irá a la base de datos. La cantidad de parametros que pasemos depende de la cantidad de la
        cantidad de parametros que hayamos pasado a la hora de crear la tabla.
        
        La palabra: 'BALON' indica que la primera casilla de la tabla tendra la informacion pasada
        El numero : '15' indica que la segunda casilla de la tabla tendra la informacion pasada
        La palabra: 'DEPORTES' indica que la tercera casilla de la tabla tendra la informacion pasada

        Si la cantidad de parametros pasados en este codigo es eccedido dara un error
    
    Tambien podemos agrupar un monton de informacion en una lista que contenga en su interior una serie
    de tuplas que se quieran llenar en esta base. Una vez creada esta lista se usara el siguiente comando para
    señalar que queremos subir la informacion de la lista a la tupla:
        nuevoCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
        
        Como vemos, ahora el metodo es executemany() y en ves de ir pasando valor por valor, solo
        colocamos un simbolo de pregunta y como segundo parametro le pasamos el nombre de la lista con la informacion

    Para obtener la informacion de la base de datos hacemos lo siguiente:
        nuevoCursor.execute("SELECT * FROM PRODUCTOS")
        variosProductos = nuevoCursor.fetchall()

        La primera linea nos devolvera lo señalado (en este caso es todo por el: *) de la base de datos
        En la segunda capturamos lo que nos haya devuelto la linea anterior con el metodo .fetchall()
        Y luego podremos maniobrar con la informacion almacenada en la variable variosProductos

    Para confirmar que queremos realizar algun cambio en la base de datos tenemos que poner el siguiente codigo:
        nuevaConexion.commit()

        Esto confirmara y agregara los cambios hechos en el codigo hacia la base dedatos.
        Sin esta linea de codigo no se realizará ningun cambio

Metodos:
    .connect()  =   Nos crea una conexion a una base de datos. Los parametros son el nombre de la base.
                    Si esta existe solo se conectará simplemente, pero si no existe, la creara.

    .cursor()   =   Crea un cursor nuevo que podemos utilizar para crear tablas

    .execute()  =   Podemos colocar varios comandos dentro de este entre comillas. Ejemplos:
                    nuevoCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
                    nuevoCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', 15, 'DEPORTES')")

    .executemany()  =   De momento solo lo he utilizado para colocar una lista como informacion la base 

    .fetchall() =   Obtiene la informacion que se le pidio anterior mente a la base de datos. Codigo de peticion:
                    nuevoCursor.execute("SELECT * FROM PRODUCTOS")

    .commit()   =   Confirma que queremos hacer modificaciones en la base de datos

    .close()    =   Cierra la base de datos que inicialmente abrimos

"""
