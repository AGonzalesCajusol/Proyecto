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
    
    
