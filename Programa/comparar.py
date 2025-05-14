def comparar_usuario(nombre, contraseña, datos_usuarios):
    for usuario in datos_usuarios:
        if usuario["Usuario"] == nombre and usuario["Contraseña"] == contraseña:
            return True
    return False
    
def comparar_nombre_dispositivo(nombre_dispositivo, datos_dispositivos):
    if nombre_dispositivo in datos_dispositivos:
        return True
    else:
        return False