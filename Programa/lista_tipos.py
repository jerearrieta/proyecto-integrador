def lista_tipos_dispositivos(msg, tipos_dispositivos):
    while True:
# Con enumerate imprimo los tipos de de dispositivos con un indice de la lista tipos_dispositivos
# para el usuario la lista empieza desde el 1 pero en realidad comienza desde el 0
        
        for i, tipo in enumerate(tipos_dispositivos, 1):
                print(f"{i}. {tipo}")
        print(f"{len(tipos_dispositivos) + 1}. Otro")
        print("0. Cancelar")
        seleccion = input(msg).strip()

        if seleccion.isdigit() and len(tipos_dispositivos) >= int(seleccion) >= 1:      
# Le restamos 1 al guardar la opcion que eligio el usuario ya que como se dijo antes se altero el indice
# para que para el usuario lo vea desde comenzando desde 1 en vez de 0
             tipo_seleccion = tipos_dispositivos[int(seleccion) - 1]
             return tipo_seleccion
        
        elif seleccion.isdigit() and len(tipos_dispositivos) + 1 == int(seleccion):
             tipo_seleccion = input("Ingrese el tipo de dispositivo: ").strip().lower()
             return tipo_seleccion
        
        elif seleccion == '0':
             return None 
        print("Error: Opcion no valida")


