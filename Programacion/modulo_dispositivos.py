# FUNCIONES (listar, buscar, agregar y eliminar)

def agregar_dispositivo(dispositivos, nombre, tipo, estado):
    while True:
        if estado not in ("encendido", "apagado"):
            return("Estado no valido")
        else:
            dispositivos[nombre] = {
                "tipo": tipo,
                "estado": estado
            }
            break
    return nombre

def eliminar_dispositivo(dispositivos, nombre):
    while True:
        if nombre in dispositivos:
            del dispositivos[nombre]
            break
        else:
            return 'Nombre inexistente'
    return f'Dispositivo "{nombre}" eliminado correctamente.'

def buscar_dispositivo(dispositivos, nombre):
    for dispositivo in dispositivos:
        if dispositivo == nombre:
            return dispositivos[dispositivo]
    else:
        return 'Nombre inexistente'


def listar_dispositivos(dispositivos):
    if dispositivos:
        return "\n".join(
            [f"Dispositivo: {nombre}\n  Tipo: {detalles['tipo']}\n  Estado: {detalles['estado']}\n"
            for nombre, detalles in dispositivos.items()]
        )
    else:
        return "No hay dispositivos registrados."