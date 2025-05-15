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
    return nombre
# print(agregar_dispositivo(dispositivos, "Calefactor", "climatización", "apagado"))

def eliminar_dispositivo(dispositivos, nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
        return f'Dispositivo "{nombre}" eliminado correctamente.'
    else:
        raise ValueError('Nombre inexistente')
# print(eliminar_dispositivo(dispositivos, nombre='Calefactor'))


def buscar_dispositivo(dispositivos, nombre):
    for dispositivo in dispositivos:
        if dispositivo == nombre:
            return dispositivos[dispositivo]
    else:
        raise ValueError('Nombre inexistente')
# print(buscar_dispositivo(dispositivos, nombre='Luz del living'))

def listar_dispositivos(dispositivos):
    if dispositivos:
        return "\n".join(
            [f"Dispositivo: {nombre}\n  Tipo: {detalles['tipo']}\n  Estado: {detalles['estado']}\n"
            for nombre, detalles in dispositivos.items()]
        )
    else:
        return "No hay dispositivos registrados."
# print(listar_dispositivos(dispositivos))