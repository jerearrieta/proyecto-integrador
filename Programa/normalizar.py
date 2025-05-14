def normalizar_nombre_dispositivo(nombre_dispositivo):
    nombre_dispositivo = nombre_dispositivo.strip().lower()

# Reemplazo los espacios por guiones bajos para evitar duplicados o redundancias
    for char in " ":
        nombre_dispositivo = nombre_dispositivo.replace(char, "_")
    return nombre_dispositivo