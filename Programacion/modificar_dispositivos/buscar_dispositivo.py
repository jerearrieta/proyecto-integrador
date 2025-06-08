from normalizar import normalizar_nombre
from dispositivos import dispositivos

def buscar_dispositivo(msg):

    nombre = input(msg).strip()
    nombre = normalizar_nombre(nombre)

    for dispositivo in dispositivos:
        if dispositivo['nombre'] == nombre:
            print("-" * 70)
            print(f" {'Nombre':<25} {'Tipo':<25}")
            print("-" * 70)            
            print(f"{dispositivo['nombre']:<25} {dispositivo['tipo']:<25}")
            print("-" * 70)
            return
    print(f"El dispositivo {nombre} no fue hallado\n")