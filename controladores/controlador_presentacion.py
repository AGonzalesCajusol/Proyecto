from bd import obtener_conexion

def nombre_presentaciones():
    conexion = obtener_conexion()
    presentaciones = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT color, talla FROM presentacion order by color asc")
        presentaciones = cursor.fetchall()
    conexion.close()
    return presentaciones

def id_presentacion_por_nombre(nombre):
    conexion = obtener_conexion()
    color, talla = nombre.split(' - ')
    id_presentacion = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM presentacion WHERE color = %s AND talla = %s", (color, talla))
        resultado = cursor.fetchone()
        if resultado:
            id_presentacion = resultado[0]
    conexion.close()
    return id_presentacion

def nombre_talla_presentacion_por_id(id_presentacion):
    conexion = obtener_conexion()
    nombre_talla_presentacion = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT color, talla FROM presentacion WHERE id = %s", (id_presentacion,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_talla_presentacion = resultado
    conexion.close()
    return nombre_talla_presentacion


def insertar_presentacion(color, talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO presentacion (color, talla) VALUES (%s, %s)', (color, talla))
    conexion.commit()
    conexion.close()

def obtener_presentaciones():
    conexion = obtener_conexion()
    presentaciones = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, color, talla FROM presentacion")
        presentaciones = cursor.fetchall()
    conexion.close()
    return presentaciones

def eliminar_presentacion(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM presentacion WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_presentacion_por_id(id):
    conexion = obtener_conexion()
    presentacion = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, color, talla FROM presentacion WHERE id = %s", (id,))
        presentacion = cursor.fetchone()
    conexion.close()
    return presentacion

def actualizar_presentacion(id, color, talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE presentacion SET color = %s, talla = %s WHERE id = %s", (color, talla, id))
    conexion.commit()
    conexion.close()
