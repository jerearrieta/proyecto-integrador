from menu import menu_automatizaciones, menu_dispositivos, menu_login, primer_menu

def main():

    login = False
    exit = False
    menu_1 = False
    menu_2 = False

    while not exit:

        if login:
           menu_1, menu_2 = primer_menu('''
            --- Bienvenido al menu de opciones. --- 
                1. Gestionar dispositivos.  
                2. Gestionar automatizaciones.  
                3. Salir.
                \n''')
        login = False

        if menu_1:
            menu_dispositivos('''
        --- Menú Dispositivos. --- 
            1. Agregar dispositivo. 
            2. Eliminar dispositivo. 
            3. Buscar dispositivo. 
            4. Listar dispositivos. 
            5. Salir.
            \n''')

        if menu_2:
            menu_automatizaciones('''
        --- Menú Automatizacion. --- 
            1. Agregar automatizacion. 
            2. Configurar automatizacion.
            3. Eliminar automatizacion. 
            4. Volver.
            \n''')
        
        login, exit = menu_login("""
    1. Loguear Usuario
    2. Registrar Usuario
    0. Salir
    \n""")

if __name__ == "__main__":
    main()