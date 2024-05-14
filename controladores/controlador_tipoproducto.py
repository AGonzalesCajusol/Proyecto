from bd import obtener_conexion

def nombres_tipoproducto():
    conexion = obtener_conexion()
    tipos_productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT  tipo FROM tipo_producto order by tipo asc")
        tipos_productos= cursor.fetchall()
    conexion.close()
    return tipos_productos

def obtener_id_por_nombre(tipo_producto):
    conexion = obtener_conexion()
    id_tipo_producto = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM tipo_producto WHERE tipo = %s", (tipo_producto,))
        resultado = cursor.fetchone()
        if resultado:
            id_tipo_producto = resultado[0]
    conexion.close()
    return id_tipo_producto


def insertar_tipoproducto(tipo, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('Insert into tipo_producto (tipo, descripcion) values (%s,%s)', (tipo,descripcion))
    conexion.commit()
    conexion.close()

def obtener_tipoproducto():
    conexion = obtener_conexion()
    tipos_productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, tipo, descripcion FROM tipo_producto")
        tipos_productos= cursor.fetchall()
    conexion.close()
    return tipos_productos

def eliminar_tipoproducto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tipo_producto WHERE id= %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_tipoproducto_id(id):
    conexion = obtener_conexion()
    tipo_producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, tipo, descripcion  FROM tipo_producto WHERE id= %s", (id,))
        tipo_producto = cursor.fetchone()
    conexion.close()
    return tipo_producto

def obtener_nombretipoproducto_id(id):
    conexion = obtener_conexion()
    tipo_producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT tipo FROM tipo_producto WHERE id= %s", (id,))
        tipo_producto = cursor.fetchone()
        if tipo_producto:
            tipo_producto = tipo_producto[0]
    conexion.close()
    return tipo_producto


def actualizar_tipoproducto(id,tipo,descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_producto  SET tipo = %s , descripcion = %s WHERE id = %s ",
                       (tipo,descripcion,id))
    conexion.commit()
    conexion.close()