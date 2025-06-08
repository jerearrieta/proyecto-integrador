from validaciones import validar_nombre, validar_numero_entero, validar_hora
from estados import obtener_estado
from imprimir import imprimir_automatizaciones, imprimir_estados
from automatizar_dispositivos.automatizaciones import automatizaciones

def configurar_automatizacion():

    imprimir_automatizaciones()

    nombre = validar_nombre("Ingrese el nombre de la automatizacion que desea configurar: ")
    auto = next((auto for auto in automatizaciones if auto['nombre'] == nombre), None)

    if not auto:    
        print(f"La automatizacion {nombre} no fue hallada.\n")
        return
    
    print("-" * 130)
    print(f" {'Nombre':<25} {'Dispositivos':<25} {'Hora Inicio':<25} {'Hora Fin':<25} {'Estado'}")
    print("-" * 130)
    dispositivo = auto['dispositivo']['nombre']
    hora_inicio = auto['hora_inicio']
    hora_fin = auto['hora_fin']
    estado = auto['estado']
    print(f"{nombre:<25} {dispositivo:<25} {hora_inicio:<25} {hora_fin:<25} {estado}")
    print("-" * 130)

    nueva_hora_inicio = validar_hora("Ingrese el horario que desea que inicie la automatizacion: ")
    nueva_hora_fin = validar_hora("Ingrese el horario que desea que finalice la automatizacion: ")

    imprimir_estados()
    cambiar_estado = validar_numero_entero("Seleccione el estado que desea que cambie automaticamente: ")
    cambiar_estado = obtener_estado(cambiar_estado - 1) 
    
    auto['hora_inicio'] = nueva_hora_inicio
    auto['hora_fin'] = nueva_hora_fin
    auto['estado'] = cambiar_estado
    print(f"La automatizacion {nombre} fue actualizada exitosamente\n")
