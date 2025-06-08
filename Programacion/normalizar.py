def normalizar_nombre(nombre):
    nombre = nombre.strip()

    for char in " ":
        nombre = nombre.replace(char, "_")
    return nombre

#REFACTORIZADO