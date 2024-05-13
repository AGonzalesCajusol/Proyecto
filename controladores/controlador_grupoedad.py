from bd import obtener_conexion

def nombres_grupo_edad():
    conexion = obtener_conexion()
    grupos_edad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT grupoedad FROM grupo_edad")
        grupos_edad = cursor.fetchall()
    conexion.close()
    return grupos_edad

def nombre_grupo_edad_por_id(id_grupo_edad):
    conexion = obtener_conexion()
    nombre_grupo_edad = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT grupoedad FROM grupo_edad WHERE id = %s", (id_grupo_edad,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_grupo_edad = resultado[0]
    conexion.close()
    return nombre_grupo_edad



def id_grupo_edad_por_nombre(nombre):
    conexion = obtener_conexion()
    id_grupo_edad = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM grupo_edad WHERE grupoedad = %s", (nombre,))
        resultado = cursor.fetchone()
        if resultado:
            id_grupo_edad = resultado[0]
    conexion.close()
    return id_grupo_edad


def insertar_grupo_edad(grupo_edad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO grupo_edad (grupoedad) VALUES (%s)', (grupo_edad,))
    conexion.commit()
    conexion.close()

def obtener_grupo_edad():
    conexion = obtener_conexion()
    grupos_edad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, grupoedad FROM grupo_edad")
        grupos_edad = cursor.fetchall()
    conexion.close()
    return grupos_edad

def eliminar_grupo_edad(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM grupo_edad WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_grupo_edad_id(id):
    conexion = obtener_conexion()
    grupo_edad = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, grupoedad FROM grupo_edad WHERE id = %s", (id,))
        grupo_edad = cursor.fetchone()
    conexion.close()
    return grupo_edad

def actualizar_grupo_edad(id, grupo_edad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE grupo_edad SET grupoedad = %s WHERE id = %s",
                       (grupo_edad, id))
    conexion.commit()
    conexion.close()
