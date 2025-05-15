#agregar en main.py automatizaciones = [diccionario], tpos_automatizaciones = [diccionario]
#eliminar inputs y ponerlos en main
def añadir_automatizacion(automatizaciones, tipos_automatizaciones):
    nombre = input("Ingrese el nombre de la automatizacion")
    print("Elija el tipo de automatizacion: \n", *tipos_automatizaciones, sep =', ')
    tipo = input("==> ")

    if tipo in tipos_automatizaciones:
        automatizaciones[nombre] = {"tipo" : tipo}

        print('Ingrese la condicion de comienzo en', *tipos_automatizaciones[tipo]["tipo_condicion"], sep =', ')
        condicion_comienzo = input(' ==> ')
        automatizaciones[nombre]["condicion_comienzo"] = condicion_comienzo

        print('Ingrese la condicion de comienzo en', *tipos_automatizaciones[tipo]["tipo_condicion"], sep =', ')
        condicion_corte = input(' ==> ')
        automatizaciones[nombre]["condicion_corte"] = condicion_corte

    else:
        print("Tipo no listado")

def eliminar_automatizacion(automatizaciones):
    eleccion = input("Seguro que desea eliminar la automatizacion? s/n ")
    if eleccion != "s" and eleccion != "n":
        print("Eleccion invalida")
    elif eleccion == "s":
        automatizaciones.clear()
eliminar_automatizacion()