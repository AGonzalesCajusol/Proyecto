from bd import obtener_conexion

def nombre_marcas():
    conexion = obtener_conexion()
    marcas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT marca FROM marca")
        marcas= cursor.fetchall()
    conexion.close()
    return marcas

def id_marca_por_nombre(nombre):
    conexion = obtener_conexion()
    id_marca = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM marca WHERE marca = %s", (nombre,))
        resultado = cursor.fetchone()
        if resultado:
            id_marca = resultado[0]
    conexion.close()
    return id_marca

def obtener_nombre_marca_por_id(id_marca):
    conexion = obtener_conexion()
    nombre_marca = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT marca FROM marca WHERE id = %s", (id_marca,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_marca = resultado[0]
    conexion.close()
    return nombre_marca


def insertar_marca(marca):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('Insert into marca(marca) values (%s)', (marca))
    conexion.commit()
    conexion.close()

def obtener_marcas():
    conexion = obtener_conexion()
    marcas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id ,marca FROM marca")
        marcas= cursor.fetchall()
    conexion.close()
    return marcas

def eliminar_marca(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM marca WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_marca_por_id(id):
    conexion = obtener_conexion()
    marca = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, marca FROM marca WHERE id= %s", (id,))
        marca = cursor.fetchone()
    conexion.close()
    return marca

def actualizar_marca(codigo, marca):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE marca SET marca = %s  WHERE id = %s",
                       (marca, codigo))
    conexion.commit()
    conexion.close()