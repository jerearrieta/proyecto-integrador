from validaciones import validar_nombre
from normalizar import normalizar_nombre
from imprimir import imprimir_automatizaciones
from automatizar_dispositivos.automatizaciones import  automatizaciones

def eliminar_automatizacion():
    imprimir_automatizaciones()
    nombre = validar_nombre("Ingrese el nombre de la automatizacion a eliminar: ")
    nombre = normalizar_nombre(nombre)

    for index, dispositivo in enumerate(automatizaciones):
        if dispositivo["nombre"] == nombre:
            automatizaciones.pop(index)
            print(f"La automatizacion {nombre} fue eliminado exitosamente\n")
            return
    print(f"La automatizacion {nombre} no fue hallado")

