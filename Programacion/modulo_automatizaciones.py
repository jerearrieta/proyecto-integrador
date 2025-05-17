def añadir_automatizacion(automatizaciones, nombre, tipo, dispositivo):
    automatizaciones[nombre] = {"tipo" : tipo}
    automatizaciones[nombre]["dispositivo"] = dispositivo

def añadir_condiciones(automatizaciones, nombre, dispositivo, condicion_comienzo, condicion_corte, estado):    
    automatizaciones[nombre]["condicion_comienzo"] = condicion_comienzo
    automatizaciones[nombre]["condicion_corte"] = condicion_corte
    automatizaciones[nombre]["estado_dispositivo"] = estado
    return f'La automatizacion {nombre} tipo {automatizaciones[nombre]["tipo"]} con la condicion de comienzo {condicion_comienzo} y condicion de cierre {condicion_corte}, que producira el estado {estado} en {dispositivo} fue establecida correctamente'

def eliminar_automatizacion(automatizaciones, eleccion):
        if eleccion not in ("s", "n"):
            print("Eleccion invalida")
        elif eleccion == "s":
            automatizaciones.clear()
            return "La automatizacion ha sido eliminada correctamente"
        else:
            return 'La automatizacion no fue eliminada'