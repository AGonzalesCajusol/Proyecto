from bd import obtener_conexion

def insertar_marca(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO marca(nombre) VALUES (%s)",
                       (codigo, nombre))
    conexion.commit()
    conexion.close()

def obtener_disqueras():
    conexion = obtener_conexion()
    disqueras = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, codigo, nombre FROM disqueras")
        disqueras = cursor.fetchall()
    conexion.close()
    return disqueras

def eliminar_disquera(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM disqueras WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_disquera_por_id(id):
    conexion = obtener_conexion()
    disquera = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, codigo, nombre FROM disqueras WHERE id = %s", (id,))
        disquera = cursor.fetchone()
    conexion.close()
    return disquera

def actualizar_disquera(codigo, nombre, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE disqueras SET codigo = %s, nombre = %s WHERE id = %s",
                       (codigo, nombre, id))
    conexion.commit()
    conexion.close()