def registrar_usuario(nombre, contraseña, datos_usuario):
    usuario = {"Usuario" : nombre, "Contraseña" : contraseña}
    datos_usuario.append(usuario)



def agregar_dispositivos(nombre_dispositivo, seleccion_tipo, datos_dispositivos):
    dispositivo = {"Nombre" : nombre_dispositivo, "Tipo" : seleccion_tipo}
    datos_dispositivos.append(dispositivo)