from modulo_menu import *

dispositivos = {
    "Luz del living": {"tipo": "luz", "estado": "apagado"},
    "Cámara puerta": {"tipo": "cámara", "estado": "encendido"}
}
tipos_dispositivos = ["luz", "camara", "televisor", "garage", "lavadora"]
automatizaciones = {}
tipos_automatizaciones = {'luz': {"tipo_condicion" : "luminosidad"},
    'temperatura': {"tipo_condicion" :"grados celsius"},
    'cortinas y ventanas' : {"tipo_condicion" : ['luminosidad', 'grados celsius']}
}

def main():
    print('--- Bienvenido al menu de opciones. ---\n 1. Gestionar Dispositivos \n 2. Gestionar automatizaciones \n 3. Salir')

    opcion = int(input(' ==> '))
    if primer_menu(opcion) == True:
        while True:
            print("--- Menú Dispositivos --- \n1. Agregar dispositivo \n2. Eliminar dispositivo \n3. Buscar dispositivo \n4. Listar dispositivos \n5. Salir")
            try:
                opcion = int(input(" ===> "))
            except ValueError:
                print("Debes ingresar un número.")
                continue

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

if __name__ == "__main__":
    main()