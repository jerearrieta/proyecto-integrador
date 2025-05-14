def validar_nombre_usuario(nombre):
    nombre = nombre.strip()

    if nombre.isalnum() and 15 >= len(nombre) >= 8:
        return True
    else:
        return False
        
def validar_contraseña_usuario(contraseña):
    contraseña = contraseña.strip()

# Como las contraseñas no pueden tener espacios valido por cada caracter de la cadena en busca de un espacio, si no existe entonces es correcto
    if all(not char.isspace() for char in contraseña) and 15 >= len(contraseña) >= 8:
        return True
    else:
        return False

def validar_nombre_dispositivo(nombre_dispositivo):

# Reemplazo los simbolos por espacios para que el if lo deje pasar, luego seran normalizados en la funcion normalizar
    for char in "-._":
        nombre_dispositivo = nombre_dispositivo.replace(char, " ")

    if all(char.isspace() or char.isalnum() for char in nombre_dispositivo): 
        return True
    else:
        return False