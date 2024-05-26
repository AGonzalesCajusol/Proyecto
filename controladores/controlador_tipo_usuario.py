from bd import obtener_conexion

def obtener_tipos_usuario():
    try:
        conexion = obtener_conexion()
        tipos_usuario = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre FROM tipo_usuario")
            tipos_usuario = cursor.fetchall()  
        conexion.close()
        return tipos_usuario   
    except Exception as e:
        print("Ocurrió un error:", e)
        return None

def insertar_tipo_usuario(nombre):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO tipo_usuario (nombre) VALUES (%s)", (nombre,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        return False

def eliminar_tipo_usuario(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM tipo_usuario WHERE id = %s", (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        return False

def obtener_tipo_usuario_por_id(id):
    try:
        conexion = obtener_conexion()
        tipo_usuario = None
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre FROM tipo_usuario WHERE id = %s", (id,))
            tipo_usuario = cursor.fetchone()
        conexion.close()
        return tipo_usuario
    except Exception as e:
        print("Ocurrió un error:", e)
        return None

def actualizar_tipo_usuario(id, nombre):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE tipo_usuario SET nombre = %s WHERE id = %s", (nombre, id))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        return False
