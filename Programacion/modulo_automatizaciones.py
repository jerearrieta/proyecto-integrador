#agregar en main.py automatizaciones = [diccionario], tpos_automatizaciones = [diccionario]
#eliminar inputs y ponerlos en main
def añadir_automatizacion(automatizaciones, tipos_automatizaciones, nombre, tipo):
    
    
    if tipo in tipos_automatizaciones:
        automatizaciones[nombre] = {"tipo" : tipo}

    else:
        print("Tipo no listado")
        
def añadir_condiciones(automatizaciones, tipos_automatizaciones, nombre, tipo, condicion_comienzo, condicion_corte):
    
    automatizaciones[nombre]["condicion_comienzo"] = condicion_comienzo

    print('Ingrese la condicion de comienzo en', *tipos_automatizaciones[tipo]["tipo_condicion"], sep =', ')
    condicion_corte = input(' ==> ')
    automatizaciones[nombre]["condicion_corte"] = condicion_corte
        
def eliminar_automatizacion(automatizaciones, eleccion):
    if eleccion != "s" and eleccion != "n":
        print("Eleccion invalida")
    elif eleccion == "s":
        automatizaciones.clear()
eliminar_automatizacion()