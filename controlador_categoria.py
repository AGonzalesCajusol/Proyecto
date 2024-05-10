from bd import obtener_conexion

def nombre_categorias():
    conexion = obtener_conexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT categoria FROM categoria")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias

def nombre_categoria_por_id(id_categoria):
    conexion = obtener_conexion()
    nombre_categoria = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT categoria FROM categoria WHERE id = %s", (id_categoria,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_categoria = resultado[0]
    conexion.close()
    return nombre_categoria


def id_categoria_por_nombre(nombre_categoria):
    conexion = obtener_conexion()
    id_categoria = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM categoria WHERE categoria = %s", (nombre_categoria,))
        resultado = cursor.fetchone()
        if resultado:
            id_categoria = resultado[0]
    conexion.close()
    return id_categoria


def insertar_categoria(categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO categoria (categoria) VALUES (%s)', (categoria,))
    conexion.commit()
    conexion.close()

def obtener_categorias():
    conexion = obtener_conexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, categoria FROM categoria")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias

def eliminar_categoria(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE id  = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_categoria_por_id(id):
    conexion = obtener_conexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, categoria FROM categoria WHERE id = %s", (id,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria

def actualizar_categoria(id, categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria SET categoria = %s WHERE id = %s", (categoria, id))
    conexion.commit()
    conexion.close()
