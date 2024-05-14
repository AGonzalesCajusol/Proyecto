from bd import obtener_conexion

def insertar_producto(nombre, precio, estado, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, nombre_imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('''
            INSERT INTO producto (nombre, precio, estado, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, enlace_imagen) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (nombre, precio, estado, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, nombre_imagen))
    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.nombre, p.precio, p.descuento, ROUND(p.precio - (p.precio * p.descuento), 2) AS precio_d, 
                p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
                p.enlace_imagen
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            ORDER BY p.id ASC;
        """)
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_producto_por_id(id_producto):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.nombre, p.precio, p.estado, p.stock, p.descripcion, p.descuento, 
            tp.tipo, g.genero, m.marca, c.categoria, ge.grupoedad, pr.color, pr.talla, p.imagen_producto
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            INNER JOIN presentacion pr ON p.id_presentacion = pr.id
            WHERE p.id = %s
        """, (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def actualizar_producto(id, nombre, precio, estado, stock, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, id_presentacion, enlace_imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, estado = %s, stock = %s, descripcion = %s, descuento = %s, id_tipo_producto = %s, id_genero = %s, id_marca = %s, id_categoria = %s, id_grupo_edad = %s, id_presentacion = %s, imagen_producto = %s WHERE id = %s",
                       (nombre, precio, estado, stock, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, id_presentacion, enlace_imagen, id))
    conexion.commit()
    conexion.close()

