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
