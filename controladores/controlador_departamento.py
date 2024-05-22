from bd import obtener_conexion

def nombre_departamentos():
    conexion = obtener_conexion()
    departamentos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT departamento FROM departamento order by departamento asc")
        departamentos = cursor.fetchall()
    conexion.close()
    return departamentos

def id_departamento_por_nombre(nombre_departamento):
    conexion = obtener_conexion()
    id_departamento = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM departamento WHERE departamento = %s", (nombre_departamento))
        resultado = cursor.fetchone()
        if resultado:
            id_departamento = resultado[0]
    conexion.close()
    return id_departamento

def nombre_departamento_por_id(id_departamento):
    conexion = obtener_conexion()
    nombre_departamento = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT departamento FROM departamento WHERE id = %s", (id_departamento))
        resultado = cursor.fetchone()
        if resultado:
            nombre_departamento = resultado
    conexion.close()
    return nombre_departamento


def insertar_departamento(departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('Insert into departamento(departamento) values (%s)', (departamento))
    conexion.commit()
    conexion.close()

def obtener_departamentos():
    conexion = obtener_conexion()
    departamentos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, departamento FROM departamento order by id asc")
        departamentos = cursor.fetchall()
    conexion.close()
    return departamentos

def eliminar_departamento(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM departamento WHERE id = %s", (id))
    conexion.commit()
    conexion.close()

def obtener_departamento_por_id(id):
    conexion = obtener_conexion()
    departamento = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, departamento FROM departamento WHERE id = %s", (id))
        departamento = cursor.fetchone()
    conexion.close()
    return departamento

def actualizar_departamento(id, departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE departamento SET departamento = %s WHERE id = %s", (departamento, id))
    conexion.commit()
    conexion.close()
