from modulo_automatizaciones import *
from modulo_dispositivos import *

def primer_menu(opcion):
    if opcion not in (1, 2, 3):
        print("Opcion invalida")
    elif opcion == 1:
        return True
    elif opcion == 2:
        return False

def menu_dispositivos(dispositivos, opcion, nombre=None, tipo=None, estado=None):
    if opcion not in (1, 2, 3, 4, 5):
        print("Opción inválida")
    elif opcion == 1:
        print(agregar_dispositivo(dispositivos, nombre, tipo, estado))
    elif opcion == 2:
        print(eliminar_dispositivo(dispositivos, nombre))
    elif opcion == 3:
        print(buscar_dispositivo(dispositivos, nombre))
    elif opcion == 4:
        print(listar_dispositivos(dispositivos))

def menu_automatizaciones(automatizaciones, tipos_automatizaciones, dispositivos, opcion, nombre, tipo, dispositivo, eleccion, condicion_comienzo, condicion_corte, estado):
    if opcion not in (1, 2, 3):
        print ("Opcion inválida")
    elif opcion == 1:
        if tipo in tipos_automatizaciones and dispositivo in dispositivos and estado in ("encendido", "apagado"):
            añadir_automatizacion(automatizaciones, nombre, tipo, dispositivo)
            print(añadir_condiciones(automatizaciones, nombre, dispositivo, condicion_comienzo, condicion_corte, estado))
        elif tipo not in tipos_automatizaciones:
            print("Tipo de automatizacion no existente")
        elif dispositivo not in dispositivos:
            print("Dispositivo no existente, agreguelo")
        elif estado not in ("encendido", "apagado"):
            print("Estado no valido")
    elif opcion == 2:
        print(eliminar_automatizacion(automatizaciones, eleccion))