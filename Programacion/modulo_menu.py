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

def menu_dispostivos(dispositivos, nombre, tipo, estado, opcion_submenu):
    print("1. Agregar Dispositivo \n2. Eliminar Dispositivo \n3. Buscar Dispositivo \n4. Listar Dispositivos \n 5. Volver")
    while True:
        if opcion_submenu not in (1, 2, 3, 4, 5):
            print("Opcion Invalida")
        elif opcion_submenu == 1:
            agregar_dispositivo(dispositivos, nombre, tipo, estado)
        elif opcion_submenu == 2:
            eliminar_dispositivo(dispositivos, nombre)
        elif opcion_submenu == 3:
            buscar_dispositivo(dispositivos, nombre)
        elif opcion_submenu == 4:
            listar_dispositivos(dispositivos)
        elif opcion_submenu == 5:
            break