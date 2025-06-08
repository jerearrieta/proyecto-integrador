from modificar_dispositivos.agregar_dispositivo import agregar_dispositivo
from modificar_dispositivos.eliminar_dispositivo import eliminar_dispositivo
from modificar_dispositivos.buscar_dispositivo import buscar_dispositivo
from modificar_dispositivos.listar_dispositivos import listar_dispositivos
from automatizar_dispositivos.añadir_automatizaciones import añadir_automatizacion
from automatizar_dispositivos.configurar_automatizacion import configurar_automatizacion
from automatizar_dispositivos.eliminar_automatizacion import eliminar_automatizacion
from validaciones import validar_nombre_usuario, validar_contraseña_usuario, introducir_opcion, introducir_opcion_2, introducir_opcion_3
from usuarios import registrar_usuario, comparar_usuario
from usuarios import datos_usuarios

def primer_menu(msg):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion(opcion):
            print("Error: Opcion no valida\n")
        if opcion == '1': 
            return True, False
        if opcion == '2':
            return False, True
        if opcion == '3':
            return False, False

def menu_dispositivos(msg):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_2(opcion):
            continue
        if opcion == '1':
            agregar_dispositivo()
        elif opcion == '2':
            eliminar_dispositivo("Ingrese el nombre del dispositivo que desea eliminar: ")
        elif opcion == '3':
            buscar_dispositivo("Ingrese el nombre del dispositivo que desea buscar: ")
        elif opcion == '4':
            listar_dispositivos()
        elif opcion == '5':
            return

def menu_automatizaciones(msg):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_3(opcion):
            continue
        elif opcion == '1':
            añadir_automatizacion()
        elif opcion == '2':
            configurar_automatizacion()
        elif opcion == '3':
            eliminar_automatizacion()
        elif opcion == '4':
            return
        
def menu_login(msg):
    while True:
        codigo = input(msg).strip()

        if codigo == '1':
            nombre = input("Ingrese el nombre de usuario (minimo 8 caracteres, maximo 15 caracteres): ")
            contraseña = input("Ingrese la contraseña: ")

            if not validar_nombre_usuario(nombre):
                print(f"El nombre {nombre} no es valido.\n")
                continue

            if not validar_contraseña_usuario(contraseña):
                print(f"La contraseña no es valida\n.")
                continue

            if comparar_usuario(nombre, contraseña, datos_usuarios):
                print("Usuario logeado con exito.\n")
                return True, False
            
            else:
                print("Error: Usuario o contraseña incorrecto\n")
                return False, False  
              
        elif codigo == '2':
            nombre = input("Ingrese el nombre de usuario (minimo 8 caracteres, maximo 15 caracteres): ")
            contraseña = input("Ingrese la contraseña (minimo 8 caracteres, maximo 15 caracteres): ")
            if not validar_nombre_usuario(nombre):
                print(f"El nombre {nombre} no es valido.\n")
                continue

            if not validar_contraseña_usuario(contraseña):
                print(f"La contraseña no es valida.\n")
                continue

            if any(u["Usuario"] == nombre for u in datos_usuarios): 
                print("Error: El usuario ya se encuentra registrado.\n")
                continue

            else:
                registrar_usuario(nombre, contraseña, datos_usuarios)
                return False, False    
                    
        elif codigo == '0':
            return False, True   
             
        else:
            print("Error: El codigo es erroneo, asegurese de no poner letras ni simbolos, solo numeros\n")

