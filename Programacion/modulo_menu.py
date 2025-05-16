from modulo_automatizaciones import *
from modulo_dispositivos import *

def primer_menu(opcion):
    while True:
        if opcion not in (1, 2, 3):
            print("Opcion invalida")
        elif opcion == 1:
            return True
        elif opcion == 2:
            return False
        else:
            break

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

def menu_automatizaciones(automatizaciones, tipos_automatizaciones, opcion, nombre, tipo, eleccion, condicion_comienzo, condicion_corte):
    if opcion not in (1, 2, 3):
        print ("Opcion inválida")
    elif opcion == 1:
        añadir_automatizacion(automatizaciones, tipos_automatizaciones, nombre, tipo)
        añadir_condiciones(automatizaciones, tipos_automatizaciones, nombre, tipo, condicion_comienzo, condicion_corte)
    elif opcion == 2:
        eliminar_automatizacion(automatizaciones, eleccion)