
def main():

    datos_usuarios = []
    datos_dispositivos = []
    tipos_dispositivos = ["luz", "camara", "televisor", "garage", "lavadora"]
    login = False
    exit = False

    while not exit:

        if login:
            menu_2(""" 
            1. Listar Dispositivos 
            2. Buscar Dispositivos
            3. Agregar Dispositivos 
            4. Eliminar Dispositivos 
            0. Cerrar Sesion""", datos_dispositivos, tipos_dispositivos)
            login = False

if __name__ == "__main__":
    main()