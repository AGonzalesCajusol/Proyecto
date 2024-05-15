from bd import obtener_conexion


def listar_detalleproducto():
    conexion = obtener_conexion()
    detalle_pr = []
    with conexion.cursor() as cursor:
        cursor.execute("select p.nombre,p.enlace_imagen, pr.color, pr.talla, dp.stock, dp.id_presentacion, dp.id_producto from detalle_presentacion dp inner join producto p on dp.id_producto = p.id inner join presentacion pr  on dp.id_presentacion = pr.id")
        detalle_pr =  cursor.fetchall()
    conexion.close()
    return detalle_pr

def insertar_detalle(id_producto, id_presentacion, stock):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # Insertar el detalle de presentación en la tabla detalle_presentacion
        cursor.execute('INSERT INTO detalle_presentacion (id_producto, id_presentacion, stock) VALUES (%s, %s, %s)', (id_producto, id_presentacion, stock))
    conexion.commit()
    conexion.close()



def eliminar_genero(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM genero WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_dp(idpre, idpro):
    conexion = obtener_conexion()
    dp = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT stock, id_presentacion, id_producto FROM detalle_presentacion WHERE id_presentacion = %s and id_producto = %s ", (idpre,idpro))
        dp = cursor.fetchone()
    conexion.close()
    return dp

def actualizar_detallepre(idpre,idpro,stock):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_presentacion SET stock = %s   WHERE id_presentacion = %s and id_producto = %s", (stock, idpre, idpro))
    conexion.commit()
    conexion.close()
