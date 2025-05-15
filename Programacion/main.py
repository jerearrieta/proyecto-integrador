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
    print('Bienvenido al menu de opciones. \n 1. Gestionar Dispositivos \n 2. Gestionar automatizaciones \n 3. Salir')
    opcion = int(input(' ==> ')
    primer_menu(opcion)



if __name__ == "__main__":
    main()