from bd import obtener_conexion

def realizar_transaccion(nombres, dni, direccion, referencia, id_distrito, estado, id_usuario, productos, tipo_comprobante, forma_pago):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO direccion_envio (nombres, dni, direccion, referencia, id_distrito) VALUES (%s, %s, %s, %s, %s)",
                (nombres, dni, direccion, referencia, id_distrito)
            )
            id_envio = cursor.lastrowid
            print("Dirección de envío registrada. ID de envío:", id_envio)
            cursor.execute(
                "INSERT INTO pedido (estado, id_usuario, id_envio) VALUES (%s, %s, %s)",
                (estado, id_usuario, id_envio)
            )
            
            id_pedido = cursor.lastrowid
            print("Pedido registrado. ID de pedido:", id_pedido)

            subtotal_total = 0.0

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
                precio, descuento = float(dsc[0]), float(dsc[1])
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
            
            # Obtener monto de envío sin IGV
            cursor.execute(
                "SELECT monto FROM distrito WHERE id = %s",
                (id_distrito,)
            )
            monto_envio = float(cursor.fetchone()[0])
            igv_envio = monto_envio * 0.18
            monto_envio_sin_igv = monto_envio - igv_envio

            # Calcular subtotales y totales
            subtotal_sin_igv = subtotal_total - (subtotal_total * 0.18)
            igv_productos = subtotal_total - subtotal_sin_igv
            igv_total = igv_productos + igv_envio
            total = subtotal_total + monto_envio

            cursor.execute(
                "INSERT INTO comprobante (monto_envio, subtotal, igv, total, tipo_comprobante, forma_pago, id_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (monto_envio_sin_igv, subtotal_sin_igv, igv_total, total, tipo_comprobante, forma_pago, id_pedido)
            )
            print("Transacción realizada exitosamente.")
        
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        conexion.close()
