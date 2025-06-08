from normalizar import normalizar_nombre
from validaciones import validar_nombre, validar_numero_entero
from imprimir import imprimir_tipos_dispositivos
from dispositivos import dispositivos
from tipos_dispositivos import tipos_dispositivos

def agregar_dispositivo():
    nombre = validar_nombre("Nombre del dispositivo: ")
    nombre_normalizado = normalizar_nombre(nombre)

    imprimir_tipos_dispositivos()
    tipo = validar_numero_entero("Seleccione un tipo de dispositivo (numerico): ")

    if not (1 <= tipo <= len(tipos_dispositivos)):
        print("Seleccion erronea, el tipo debe estar dentro del rango\n")
        return
    
    tipo_final = tipos_dispositivos[tipo - 1]

    if any(u["nombre"] == nombre_normalizado for u in dispositivos):
            print(f"El dispositivo {nombre_normalizado} ya se encuentra registrado.\n")
            return
    
    nuevo_dispositivo = {"nombre" : nombre_normalizado, "tipo" : tipo_final}

    dispositivos.append(nuevo_dispositivo)

    print(f"Dispositivo {nombre_normalizado} agregado correctamente.\n")
