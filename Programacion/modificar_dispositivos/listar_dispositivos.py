from dispositivos import  dispositivos

def listar_dispositivos():
    print("-" * 70)
    print(f" {'Nombre':<25} {'Tipo':<25}")
    print("-" * 70)

    for dispositivo in dispositivos:
        nombre = dispositivo.get("nombre")
        tipo = dispositivo.get("tipo") 

        print(f"{nombre:<25} {tipo:<25}")
        print("-" * 70)
