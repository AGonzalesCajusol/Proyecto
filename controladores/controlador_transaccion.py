from bd import obtener_conexion

# def direccionenvio (nombres,dni,direccion,referencia,id_distrito):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("insert into direccion_envio(nombres,dni,direccion,referencia,id_distrito) values (%s,%s,%s,%s,%s)",(nombres,dni,direccion,referencia ,id_distrito))
#     id = cursor.lastrowid
#     conexion.commit()
#     conexion.close()
#     return id
# def pedido(fecha_pedido,hora_pedido,estado,id_usuario,id_dr):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("insert into pedido (fecha_pedido,hora_pedido,estado,id_usuario,id_envio) values (%s,%s,%s,%s,%s)",(fecha_pedido,hora_pedido,estado,id_usuario,id_dr))
#     id = cursor.lastrowid
#     conexion.commit()
#     conexion.close()
#     return id
# def detalle_pedido(fecha_pedido,hora_pedido,precio,cantidad,subtotal,id_producto,id_pedido):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("insert detalle_pedido (fecha_pedido,hora_pedido,precio,cantidad,subtotal,id_producto,id_pedido) values (%s,%s,%s,%s,%s)",(fecha_pedido,hora_pedido,precio,cantidad,subtotal,id_producto,id_pedido))
#     conexion.commit()
#     conexion.close()
def comprabante(fecha,monto_envio,subtotal,igv,total,tipo_comprobante,forma_pago,id_pedido):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("insert comprobante (fecha,hora,monto_envio,subtotal,igv,total,tipo_comprobante,forma_pago,id_pedido) values (%s,%s,%s,%s,%s)",(fecha,monto_envio,subtotal,igv,total,tipo_comprobante,forma_pago,id_pedido))
    conexion.commit()
    conexion.close()
def disminuit_stock(id_pre,cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # Consultar el stock actual del producto
        cursor.execute("SELECT stock FROM detalle_presentacion WHERE id = %s", (id_pre))
        stock_actual = cursor.fetchone()[0]

        # Verificar si hay suficiente stock para la venta
        if stock_actual < cantidad:
            raise ValueError("No hay suficiente stock disponible")

        # Calcular el nuevo stock después de la venta
        nuevo_stock = stock_actual - cantidad

        # Actualizar el stock en la base de datos
        cursor.execute("UPDATE detalle_presentacion SET stock = %s WHERE id = %s", (nuevo_stock, id_pre))
    conexion.commit()
    conexion.close()

def realizar_transaccion(nombres, dni, direccion, referencia, id_distrito, estado, id_usuario, productos, tipo_comprobante, forma_pago):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO direccion_envio (nombres, dni, direccion, referencia, id_distrito) VALUES (%s, %s, %s, %s, %s)",
                (nombres, dni, direccion, referencia, id_distrito)
            )
            id_envio = cursor.lastrowid

            cursor.execute(
                "INSERT INTO pedido (estado, id_usuario, id_envio) VALUES (%s, %s, %s)",
                (estado, id_usuario, id_envio)
            )
            id_pedido = cursor.lastrowid

            subtotal_total = 0

            for producto in productos:
                talla = producto.get('talla')
                color = producto.get('color')
                cantidad = producto.get('cantidad')
                id_producto = producto.get('id')

                cursor.execute(
                    "SELECT id FROM presentacion WHERE color = %s AND talla = %s",
                    (color, talla)
                )
                id_pre = cursor.fetchone()
                if not id_pre:
                    raise ValueError("No se encontró la presentación para el color {} y la talla {}".format(color, talla))
                id_pre = id_pre[0]

                cursor.execute(
                    "SELECT stock FROM detalle_presentacion WHERE id_presentacion = %s AND id_producto = %s",
                    (id_pre, id_producto)
                )
                stock = cursor.fetchone()
                if not stock:
                    raise ValueError("No se encontró el detalle de la presentación para el id_presentacion {} y el id_producto {}".format(id_pre, id_producto))
                stock = stock[0]

                if cantidad > stock:
                    raise ValueError("No hay suficiente stock disponible para el producto {} en la presentación {}".format(id_producto, id_pre))

                cursor.execute(
                    "SELECT precio, descuento FROM producto WHERE id = %s",
                    (id_producto,)
                )
                dsc = cursor.fetchone()
                if not dsc:
                    raise ValueError("No se encontró el producto con id {}".format(id_producto))
                precio, descuento = dsc
                descuento = precio * descuento
                subtotal = (precio - descuento) * cantidad
                subtotal_total += subtotal

                cursor.execute(
                    "INSERT INTO detalle_pedido (precio, descuento, cantidad, subtotal, id_producto, id_pedido) VALUES (%s, %s, %s, %s, %s, %s)",
                    (precio, descuento, cantidad, subtotal, id_producto, id_pedido)
                )

                cursor.execute(
                    "UPDATE detalle_presentacion SET stock = stock - %s WHERE id_presentacion = %s",
                    (cantidad, id_pre)
                )

            cursor.execute(
                "SELECT monto FROM distrito WHERE id = %s",
                (id_distrito,)
            )
            monto_envio = cursor.fetchone()[0]

            subtotal_con_envio = subtotal_total + monto_envio
            igv = round(subtotal_con_envio * 0.18, 2)
            total = subtotal_con_envio + igv

            cursor.execute(
                "INSERT INTO comprobante (monto_envio, subtotal, igv, total, tipo_comprobante, forma_pago, id_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (monto_envio, subtotal_total, igv, total, tipo_comprobante, forma_pago, id_pedido)
            )

        conexion.commit()

    except Exception as e:
        conexion.rollback()
        raise e

    finally:
        conexion.close()