from bd import obtener_conexion

def nombre_generos():
    conexion = obtener_conexion()
    generos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT genero FROM genero order by genero asc")
        generos = cursor.fetchall()
    conexion.close()
    return generos

def obtener_nombre_genero_por_id(id_genero):
    conexion = obtener_conexion()
    nombre_genero = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT genero FROM genero WHERE id = %s", (id_genero,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_genero = resultado[0]
    conexion.close()
    return nombre_genero


def id_genero_por_nombre(nombre):
    conexion = obtener_conexion()
    id_genero = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM genero WHERE genero = %s", (nombre,))
        resultado = cursor.fetchone()
        if resultado:
            id_genero = resultado[0]
    conexion.close()
    return id_genero


def insertar_genero(genero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO genero (genero) VALUES (%s)', (genero,))
    conexion.commit()
    conexion.close()

def obtener_generos():
    conexion = obtener_conexion()
    generos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, genero FROM genero")
        generos = cursor.fetchall()
    conexion.close()
    return generos

def eliminar_genero(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM genero WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_genero_por_id(id):
    conexion = obtener_conexion()
    genero = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, genero FROM genero WHERE id = %s", (id,))
        genero = cursor.fetchone()
    conexion.close()
    return genero

def actualizar_genero(id, genero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE genero SET genero = %s WHERE id = %s", (genero, id))
    conexion.commit()
    conexion.close()
