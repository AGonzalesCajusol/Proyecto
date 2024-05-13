from bd import obtener_conexion

def nombres_tipoproducto(usuario, password):
    try:
        conexion = obtener_conexion()
        tipos_productos = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT usuario, contraseña FROM usuario WHERE usuario = %s AND contraseña = %s AND estado = 'A' ", (usuario,password))
            tipos_productos = cursor.fetchone()  
        conexion.close()
        return tipos_productos   
    except Exception as e:
        print("Ocurrió un error:", e)
        return None
    
def insertar_usuario(numdocumento, apellidos, nombres, telefono, correo, usuario, contraseña, estado, id_tipo_usuario):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuario (numdocumento, apellidos, nombres, telefono, correo, usuario, contraseña, estado, id_tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (numdocumento, apellidos, nombres, telefono, correo, usuario, contraseña, estado, id_tipo_usuario))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Ocurrió un error:", e)


def usuario(email,contraseña):
    try:
        nombres = []
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute( "select nombres from usuario where correo= %s and contraseña = %s",(email,contraseña))
        nombres = cursor.fetchall()
        conexion.close()
        return nombres
    except Exception as e:
        print("Ocurrió un error:", e)
