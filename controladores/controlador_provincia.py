from flask import render_template
from bd import obtener_conexion

def nombre_provincias():
    conexion = obtener_conexion()
    provincias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT provincia, id_departamento FROM provincia order by provincia asc")
        provincias = cursor.fetchall()
    conexion.close()
    return provincias

def nombre_provinciasxdepartamento(id_departamento):
    conexion = obtener_conexion()
    provincias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT provincia FROM provincia where id_departamento  = %s", (id_departamento))
        provincias = cursor.fetchall()
    conexion.close()
    return provincias



def id_provincia_por_nombre(nombre):
    conexion = obtener_conexion()
    provincia, departamento = nombre.split(' - ')
    id_provincia = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id FROM provincia WHERE provincia = %s AND id_departamento = %s", (provincia, departamento))
        resultado = cursor.fetchone()
        if resultado:
            id_provincia = resultado[0]
    conexion.close()
    return id_provincia

def nombre_departamento_provincia_por_id(id_provincia):
    conexion = obtener_conexion()
    nombre_departamento_provincia = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT provincia, id_departamento FROM provincia WHERE id = %s", (id_provincia))
        resultado = cursor.fetchone()
        if resultado:
            nombre_departamento_provincia = resultado
    conexion.close()
    return nombre_departamento_provincia


##anggelo
def obtener_departamentos():
    conexion = obtener_conexion()
    departamentos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, departamento FROM departamento ORDER BY departamento ASC")
        departamentos = cursor.fetchall()
    conexion.close()
    return departamentos

def insertar_provincia(provincia, id_departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO provincia (provincia, id_departamento) VALUES (%s, %s)', (provincia, id_departamento))
    conexion.commit()
    conexion.close()
## anggelo

def obtener_provincia():
    conexion = obtener_conexion()
    provinciaes = []
    with conexion.cursor() as cursor:
        cursor.execute('''
                       SELECT pr.id, pr.provincia, de.departamento FROM provincia pr inner join departamento de
                        on pr.id_departamento = de.id         
                       ''' )
        provinciaes = cursor.fetchall()
    conexion.close()
    return provinciaes

def eliminar_provincia(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM provincia WHERE id = %s", (id))
    conexion.commit()
    conexion.close()

def obtener_provincia_por_id(id):
    conexion = obtener_conexion()
    provincia = None
    with conexion.cursor() as cursor:
        cursor.execute('SELECT pr.id, pr.provincia, de.departamento FROM provincia pr inner join departamento de on pr.id_departamento = de.id   where pr.id=%s', (id))
        provincia = cursor.fetchone()
    conexion.close()
    return provincia

def actualizar_provincia(id, provincia, departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE provincia SET provincia = %s, id_departamento = %s WHERE id = %s", (provincia, departamento, id))
    conexion.commit()
    conexion.close()

#-----------anggelo 
def obtener_departamentos():
    conexion = obtener_conexion()
    departamentos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, departamento FROM departamento ORDER BY departamento ASC")
        departamentos = cursor.fetchall()
    conexion.close()
    return departamentos

#--------- anggelo
