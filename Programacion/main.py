from modulo_menu import *

dispositivos = {
    "Luz del living": {"tipo": "luz", "estado": "apagado"},
    "Cámara puerta": {"tipo": "cámara", "estado": "encendido"}
}
tipos_dispositivos = ["luz", "camara", "televisor", "garage", "lavadora"]
automatizaciones = {}
tipos_automatizaciones = {'luz': {"tipo_condicion" : "luminosidad"},
    'temperatura': {"tipo_condicion" :"grados celsius"},
    'cortinas' : {"tipo_condicion" : 'luminosidad'},
    'ventanas' : {"tipo_condicion" : 'grados celsius'}
}

def introducir_opcion():
    try:
        opcion = int(input(" ===> "))
    except ValueError:
        print("Debes ingresar un número.")
    return opcion

def main():
    print('--- Bienvenido al menu de opciones. ---\n 1. Gestionar dispositivos \n 2. Gestionar automatizaciones \n 3. Salir')

    opcion = int(input(' ==> '))
    if primer_menu(opcion) == True:
        while True:
            print("--- Menú Dispositivos --- \n1. Agregar dispositivo \n2. Eliminar dispositivo \n3. Buscar dispositivo \n4. Listar dispositivos \n5. Salir")
            opcion = introducir_opcion()

            if opcion == 5:
                break

            nombre = tipo = estado = None

            if opcion == 1:
                nombre = input("Nombre del dispositivo: ")
                tipo = input("Tipo del dispositivo: ")
                estado = input("Estado del dispositivo (Encendido/Apagado): ").lower()
            elif opcion in (2, 3):
                nombre = input("Nombre del dispositivo: ")

            menu_dispositivos(dispositivos, opcion, nombre, tipo, estado)
    else:
        while True:
            print("--- Menú Automatizacion --- \n1. Agregar automatizacion \n2. Eliminar automatizacion \n3. Volver")
            opcion = introducir_opcion()

            if opcion == 3:
                break
            
            nombre = tipo = dispositivo = eleccion = condicion_comienzo = condicion_corte = estado = None
            if opcion == 1:
                nombre = input("Introduzca el nombre de la automatizacion \n===> ")
                print("Elija el tipo de automatizacion: \n", *tipos_automatizaciones, sep =', ')
                tipo = input(" ===> ")
                dispositivo = input("Ingrese el dispositivo a manipular ==> ")
                print('Ingrese la condicion de comienzo en', tipos_automatizaciones[tipo]["tipo_condicion"])
                condicion_comienzo = input(' ==> ')
                print('Ingrese la condicion de corte en', tipos_automatizaciones[tipo]["tipo_condicion"])
                condicion_corte = input(' ==> ')
                estado = input("Ingrese el estado en el que debe estar el dispositivo cuando la condicion se cumpla (Encendido/Apagado) \n ===> ").lower()
            
            elif opcion == 2:
                eleccion = input("Desea eliminar la actualizacion s/n \n===> ")
            
            menu_automatizaciones(automatizaciones, tipos_automatizaciones, dispositivos, opcion, nombre, tipo, dispositivo, eleccion, condicion_comienzo, condicion_corte, estado)
if __name__ == "__main__":
    main()