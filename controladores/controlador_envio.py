from bd import obtener_conexion

def insertar_direccion_envio(nombres, direccion, montoenvio, referencia, tipo_envio, id_distrito):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO direccion_envio (nombres, direccion, montoenvio, referencia, tipo_envio, id_distrito) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nombres, direccion, montoenvio, referencia, tipo_envio, id_distrito))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Ocurrió un error:", e)


def monto_envio(distrito, provincia, departamento):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('''select  monto from distrito  inner join provincia
            on provincia.id = distrito.id_provincia inner join departamento
            on departamento.id = provincia.id_departamento
            where distrito.distrito = %s AND provincia.provincia = %s and departamento.departamento= %s ''',(distrito,provincia,departamento))
            dato = cursor.fetchone()
        conexion.close()
        return dato
    except Exception as e:
        print("Ocurrió un error:", e)


