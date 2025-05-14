# FUNCIONES (listar, buscar, agregar y eliminar)
dispositivos = {
    "Luz del living": {"tipo": "luz", "estado": "apagado"},
    "Cámara puerta": {"tipo": "cámara", "estado": "encendido"}
}

def agregar_dispositivo(dispositivos, nombre, tipo, estado):
    dispositivos[nombre] = {
        "tipo": tipo,
        "estado": estado
    }
    return nombre  # Retornamos el nombre del dispositivo agregado
print(agregar_dispositivo(dispositivos, "Calefactor", "climatización", "apagado"))

def eliminar_dispositivo(dispositivos, nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
    else:
        raise ValueError('ID Inexistente')
    
print(eliminar_dispositivo(dispositivos, nombre='Calefactor'))


def buscar_dispositivo(dispositivos, nombre):
    for id_dispositivo in dispositivos:
        dispositivo = dispositivos[id_dispositivo]
        if dispositivo['nombre'] == nombre:
            return dispositivo  # Devolvemos todo el diccionario del dispositivo
    else:
        raise ValueError('Nombre inexistente')

# print(buscar_dispositivo(dispositivos, nombre='Ventilador'))
