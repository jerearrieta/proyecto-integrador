def añadir_automatizacion(automatizaciones, tipos_automatizaciones, nombre, tipo):
    if tipo in tipos_automatizaciones:
        automatizaciones[nombre] = {"tipo" : tipo}
    else:
        print("Tipo no listado")

def añadir_condiciones(automatizaciones, nombre, condicion_comienzo, condicion_corte):    
    automatizaciones[nombre]["condicion_comienzo"] = condicion_comienzo
    automatizaciones[nombre]["condicion_corte"] = condicion_corte

def eliminar_automatizacion(automatizaciones, eleccion):
    if eleccion not in ("s", "n"):
        print("Eleccion invalida")
    elif eleccion == "s":
        automatizaciones.clear()