import sqlite3

conexion = sqlite3.connect("CRUD.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM DATOS_USUARIOS")

conexion.commit()

conexion.close()
