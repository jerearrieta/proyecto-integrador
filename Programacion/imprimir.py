from dispositivos import dispositivos
from estados import estados
from tipos_dispositivos import tipos_dispositivos
from automatizar_dispositivos.automatizaciones import automatizaciones

def imprimir_dispositivos():
    print("-" * 20)
    print(f" {'Dispositivos':<25}")
    print("-" * 20)
    for i, valor in enumerate(dispositivos):
        if "nombre" in valor:
            print(f"{i + 1}. {valor['nombre']}")
            print("-" * 20)
    print("\n")

def imprimir_estados():
    print("-" * 20)
    print(f" {'Estados':<25}")
    print("-" * 20)
    for i, clave in enumerate(estados):
        print(f"{i + 1}. {estados[clave]}")
        print("-" * 20)
    print("\n")

def imprimir_tipos_dispositivos():
    print("-" * 20)
    print(f" {'Tipo':<25}")
    print("-" * 20)
    for i in range(len(tipos_dispositivos)):
        print(f"{i + 1}. {tipos_dispositivos[i]}")
        print("-" * 20)
    print("\n")

def imprimir_automatizaciones():
    print("-" * 130)
    print(f" {'Nombre':<25} {'Dispositivos':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}")
    print("-" * 130)
    for auto in automatizaciones:
        nombre = auto['nombre']
        dispositivo = auto['dispositivo']['nombre'] 
        hora_inicio = auto['hora_inicio']
        hora_fin = auto['hora_fin']
        estado = auto['estado']

        print(f"{nombre:<25} {dispositivo:<25} {hora_inicio:<25} {hora_fin:<25}  {estado}")
        print("-" * 130)
    print("\n")
