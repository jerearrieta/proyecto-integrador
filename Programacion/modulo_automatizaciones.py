def añadir_automatizacion(automatizaciones, tipos_automatizaciones, nombre, tipo):
    while True:
        if tipo in tipos_automatizaciones:
            automatizaciones[nombre] = {"tipo" : tipo}
            break
        else:
            print("Tipo no listado")

def añadir_condiciones(automatizaciones, nombre, condicion_comienzo, condicion_corte):    
    automatizaciones[nombre]["condicion_comienzo"] = condicion_comienzo
    automatizaciones[nombre]["condicion_corte"] = condicion_corte
    return f'La automatizacion {nombre} tipo {automatizaciones[nombre]["tipo"]} con la condicion de comienzo {condicion_comienzo} y condicion de cierre {condicion_corte} fue establecida correctamente'

def eliminar_automatizacion(automatizaciones, eleccion):
    while True:
        if eleccion not in ("s", "n"):
            print("Eleccion invalida")
        elif eleccion == "s":
            automatizaciones.clear()
            break
    return "La automatizacion ha sido eliminada correctamente"