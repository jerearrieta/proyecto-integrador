from normalizar import normalizar_nombre
from validaciones import validar_numero_entero, validar_nombre, validar_hora
from estados import obtener_estado
from imprimir import imprimir_dispositivos, imprimir_estados
from automatizar_dispositivos.automatizaciones import automatizaciones
from dispositivos import dispositivos
from estados import estados


def añadir_automatizacion():

    nombre = normalizar_nombre(validar_nombre("Introduzca el nombre de la automatizacion: "))
    imprimir_dispositivos()
    dispositivo_indice = validar_numero_entero("Seleccione un dispositivo: ")
    if not dispositivo_indice <= len(dispositivos):
        print("Error: Ingrese uno de los numeros listados que sean validos\n")
        return
    imprimir_estados()
    estado_indice = validar_numero_entero("Seleccione un estado: ")
    if not estado_indice <= len(estados):
        print("Error: Ingrese uno de los numeros listados que sean validos\n")
        return
    hora_inicio = validar_hora("Ingrese el horario el cual debe de iniciar la accion (Use el horario militar, es decir, 8:30PM => 2030): ")
    hora_fin = validar_hora("Ingresar el horario el cual debe de finalizar la accion (Use el horario militar, es decir, 8:30PM => 2030):")

    dispositivo = dispositivos[dispositivo_indice - 1]
    estado_final = obtener_estado(estado_indice - 1)
                
    nueva_automatizacion = {"nombre" : nombre, "dispositivo" : dispositivo, "estado" : estado_final, "hora_inicio" : hora_inicio, "hora_fin" : hora_fin}
    automatizaciones.append(nueva_automatizacion)

    print("-" * 130)
    print(f"{'Nombre':<25} {'Dispositivo':<25} {'Hora Inicio':<25} {'Hora_Fin':<25} {'Estado'}")
    print("-" * 130)
    print(f"{nombre:<25} {dispositivo['nombre']:<25} {hora_inicio:<25} {hora_fin:<25} {estado_final}")
    print("-" * 130)
