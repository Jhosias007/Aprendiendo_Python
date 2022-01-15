
def devuelveCiudades(*ciudades):    # el asterisco antes de ponerle parametros a la funcion o generador
                                    # permiten poner la cantidad que se quiera al ser llamada
    for elementos in ciudades:
        #for subElementos in elementos:  # un for dentro de otro for me permite tomar elementos dentro de un elemento
                                        # por ejemplo, tomar el caracter de una palabra
        
        yield from elementos    # con yield from podemos evitar crear mas bucles dentro de otros para acceder a
                                # elementos dentro de otros elementos
            

ciudadesDevueltas = devuelveCiudades("Lima", "Madrid", "Barcelona", "Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

