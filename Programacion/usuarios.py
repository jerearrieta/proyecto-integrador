datos_usuarios = [{"Usuario": "Administrador", "Contraseña" : "Administrador"}]

def registrar_usuario(nombre, contraseña, datos_usuario):
    usuario = {"Usuario" : nombre, "Contraseña" : contraseña}
    datos_usuario.append(usuario)

def comparar_usuario(nombre, contraseña, datos_usuarios):
    for usuario in datos_usuarios:
        if usuario["Usuario"] == nombre and usuario["Contraseña"] == contraseña:
            return True
    return False
    