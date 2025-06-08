estados = {0: "MANTENIMIENTO", 1 : "APAGADO", 2 : "AHORRO_DE_ENERGIA", 3 : "ENCENDIDO"}

def obtener_estado(clave):
    if clave in estados:
        return estados[clave]

#REFACTORIZADO