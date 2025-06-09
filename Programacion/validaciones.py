def validar_nombre(msg):
    while True:
        valor = input(msg).lower().strip()
        if all(char.isalpha() or char.isspace() for char in valor):
            return valor
        print("Nombre de automatizacion no valido, recuerde que los simbolos no son validos.\n")

def validar_numero_entero(msg):
    while True:
        numero = input(msg)
        if numero.isdigit() and int(numero) > 0:
            return int(numero)
        print("Ingrese un numero valido\n")

def validar_numero_flotante(msg):
    while True:
        numero = input(msg)
        if numero.isdigit().count(".") <= 1 and int(numero) > 0:
            return float(numero)
        print("Ingrese un numero valido\n")

def validar_nombre_usuario(nombre):
    nombre = nombre.strip()

    if nombre.isalnum() and 15 >= len(nombre) >= 8:
        return True
    else:
        return False
    
def validar_contraseña_usuario(contraseña):
    contraseña = contraseña.strip()

    if all(not char.isspace() for char in contraseña) and 15 >= len(contraseña) >= 8:
        return True
    else:
        return False
    
def validar_nombre_dispositivo(nombre_dispositivo):
    for char in "-._":
        nombre_dispositivo = nombre_dispositivo.replace(char, " ")

    if all(char.isspace() or char.isalnum() for char in nombre_dispositivo): 
        return True
    else:
        return False

def validar_hora(msg):
    numero = validar_numero_entero(msg)
    if len(str(numero)) == 4:
        if 1000 <= numero <= 2359:
            hora = numero // 100
            minutos = numero % 100

            if minutos >= 0 and minutos < 60:
                if hora == 0:
                    return (f"12:{minutos:02d} AM")
                elif hora < 12:
                    return (f"{hora:02d}:{minutos:02d} AM")
                elif hora == 12:
                    return (f"12:{minutos:02d} PM")
                else:
                    return (f"{hora - 12:02d}:{minutos:02d} PM")
            else:
                print(f"Minutos fuera del rango (0-59)")
        else:
            print(f"La hora {numero} no es valida")
    else:
        print(f"El numero {numero} debe de tener 4 digitos para poder calcularlo\n")



#
##
### VALIDACIONES DE ENTRADAS DE LOS MENU'S
##
#

def introducir_opcion(valor):
        if valor.isdigit() and 4 > int(valor) > 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

def introducir_opcion_2(valor): 
        if valor.isdigit() and 6 > int(valor) > 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

def introducir_opcion_3(valor):
        if valor.isdigit() and 5 > int(valor) > 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

