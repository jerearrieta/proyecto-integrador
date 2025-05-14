from validar import validar_nombre_usuario, validar_contraseña_usuario, validar_nombre_dispositivo
from comparar import comparar_usuario
from registrar import registrar_usuario, agregar_dispositivos
from normalizar import normalizar_nombre_dispositivo
from lista_tipos import lista_tipos_dispositivos

def menu(msg, datos_usuarios):
    while True:
        codigo = input(msg).strip()

        if codigo == '1':
            nombre = input("Ingrese el nombre de usuario (minimo 8 caracteres, maximo 15 caracteres): ")
            contraseña = input("Ingrese la contraseña: ")

# Usando el not hace que cuando el nombre del usuario sea verdadero se cambie a falso y no entre al if reduciendo los anillados de if's 
# en caso de que el nombre ya exista nos dara falso (el not lo convertira a verdadero) y entrara al if para imprimir el mensaje y ejecutara
# el continue que hara que vuelva al inicio del bucle en vez de un break/return que hace que lo saque del bucle           
            if not validar_nombre_usuario(nombre):
                print(f"El nombre {nombre} no es valido.")
                continue

            if not validar_contraseña_usuario(contraseña):
                print(f"La contraseña no es valida.")
                continue

            if comparar_usuario(nombre, contraseña, datos_usuarios):
                print("Usuario logeado con exito.")
# Los return (True, False) son para las banderas de "login" y "exit" que controlan los menu's en main, se lee primero el login 
# (True si se logeo con exito, False si se fallo) y segundo el exit (True si quiere salir del programa, False si desea continuar)
                return True, False
            
            else:
                print("Error: Usuario o contraseña incorrecto")
                return False, False  
              
        elif codigo == '2':
            nombre = input("Ingrese el nombre de usuario (minimo 8 caracteres, maximo 15 caracteres): ")
            contraseña = input("Ingrese la contraseña: ")
            if not validar_nombre_usuario(nombre):
                print(f"El nombre {nombre} no es valido.")
                continue

            if not validar_contraseña_usuario(contraseña):
                print(f"La contraseña no es valida.")
                continue

# Por cada iteracion en la lista "datos_usuarios" recorrera cada diccionario que tenga como clave "Usuario" comparando si el nombre ingresado
# por el usuario es igual o no, en caso de que sea verdadero entrara al if, imprimira un mensaje de "Usuario ya registrado" y volvera al inicio
# del bucle principal, caso contrario procedera a registrarlo           
            if any(u["Usuario"] == nombre for u in datos_usuarios): 
                print("Error: El usuario ya se encuentra registrado.")
                continue

            else:
                registrar_usuario(nombre, contraseña, datos_usuarios)
                return False, False    
                    
        elif codigo == '0':
            return False, True   
             
        else:
            print("Error: El codigo es erroneo, asegurese de no poner letras ni simbolos, solo numeros")

def menu_2(msg, datos_dispositivos, tipos_dispositivos):
    while True:
        codigo = input(msg).strip()

        if codigo == '1':
            listar_dispositivos()
        elif codigo == '2':
            buscar_dispositivos()
        elif codigo == '3':
            nombre_dispositivo = input("Escribe el nombre del dispositivo a agregar: ")
            if not validar_nombre_dispositivo(nombre_dispositivo):
                print(f"El nombre {nombre_dispositivo} no es valido.")
                continue 
            nombre_dispositivo = normalizar_nombre_dispositivo(nombre_dispositivo)
            if any(u["Nombre"] == nombre_dispositivo for u in datos_dispositivos):
                print(f"El dispositivo {nombre_dispositivo} ya se encuentra registrado.")
                continue

            seleccion_tipo = lista_tipos_dispositivos("Seleccione una opcion: ", tipos_dispositivos)
            if seleccion_tipo is not None:
                agregar_dispositivos(nombre_dispositivo, seleccion_tipo, datos_dispositivos)
            else:
                print("Error: No elegiste ningun tipo")
                continue

        elif codigo == '4':
            eliminar_dispositivos()
        elif codigo == '0':
            return False
        else:
            print("Error: El codigo es erroneo, asegurese de no poner letras ni simbolos, solo numeros")



