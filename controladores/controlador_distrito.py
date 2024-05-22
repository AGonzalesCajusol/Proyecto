from bd import obtener_conexion

def nombre_distritos():
    conexion = obtener_conexion()
    distritos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT distrito, id_provincia FROM distrito order by distrito asc")
        distritos = cursor.fetchall()
    conexion.close()
    return distritos

def id_distrito_por_nombre(nombre):
    conexion = obtener_conexion()
    distrito, provincia = nombre.split(' - ')
    id_distrito = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM distrito WHERE distrito = %s AND id_provincia = %s", (distrito, provincia))
        resultado = cursor.fetchone()
        if resultado:
            id_distrito = resultado[0]
    conexion.close()
    return id_distrito

def nombre_provincia_distrito_por_id(id_distrito):
    conexion = obtener_conexion()
    nombre_provincia_distrito = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT distrito, id_provincia FROM distrito WHERE id = %s", (id_distrito))
        resultado = cursor.fetchone()
        if resultado:
            nombre_provincia_distrito = resultado
    conexion.close()
    return nombre_provincia_distrito


def insertar_distrito(distrito, provincia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO distrito (distrito, id_provincia) VALUES (%s, %s)', (distrito, provincia))
    conexion.commit()
    conexion.close()

def obtener_distrito():
    conexion = obtener_conexion()
    distritoes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, distrito, id_provincia FROM distrito")
        distritoes = cursor.fetchall()
    conexion.close()
    return distritoes

def eliminar_distrito(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM distrito WHERE id = %s", (id))
    conexion.commit()
    conexion.close()

def obtener_distrito_por_id(id):
    conexion = obtener_conexion()
    distrito = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, distrito, id_provincia FROM distrito WHERE id = %s", (id))
        distrito = cursor.fetchone()
    conexion.close()
    return distrito

def actualizar_distrito(id, distrito, provincia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE distrito SET distrito = %s, id_provincia = %s WHERE id = %s", (distrito, provincia, id))
    conexion.commit()
    conexion.close()
