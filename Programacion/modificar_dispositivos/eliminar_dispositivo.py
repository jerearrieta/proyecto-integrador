from normalizar import normalizar_nombre
from dispositivos import dispositivos

def eliminar_dispositivo(msg):

    nombre = input(msg).strip()
    nombre = normalizar_nombre(nombre)

    for index, dispositivo in enumerate(dispositivos):
        if dispositivo["nombre"] == nombre:
            dispositivos.pop(index)
            print(f"El dispositivo {nombre} fue eliminado exitosamente\n")
            return
    print(f"El dispositivo {nombre} no fue hallado\n")

#REFACTORIZADO