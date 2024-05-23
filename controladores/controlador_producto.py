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


def obtener_calzados():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT p.id, p.nombre, p.precio, p.descuento, ROUND(p.precio - (p.precio * p.descuento), 2) AS precio_d, 
                p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
                p.enlace_imagen, pr.color
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            INNER JOIN detalle_presentacion dp ON p.id = dp.id_producto
            INNER JOIN presentacion pr ON pr.id = dp.id_presentacion
            WHERE c.categoria = "Calzado" 
            ORDER BY p.id ASC;
        """)
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_modahombre():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT p.id, p.nombre, p.precio, p.descuento, ROUND(p.precio - (p.precio * p.descuento), 2) AS precio_d, 
                p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
                p.enlace_imagen,pr.color
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            INNER JOIN detalle_presentacion dp ON p.id = dp.id_producto
            INNER JOIN presentacion pr ON pr.id = dp.id_presentacion
            WHERE c.categoria = "Ropa Hombre" 
            ORDER BY p.id ASC;

        """)
        productos = cursor.fetchall()
    conexion.close()
    return productos




def obtener_ropaniños():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT p.id, p.nombre, p.precio, p.descuento, ROUND(p.precio - (p.precio * p.descuento), 2) AS precio_d, 
                p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
                p.enlace_imagen, pr.color
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            INNER JOIN detalle_presentacion dp ON p.id = dp.id_producto
            INNER JOIN presentacion pr ON pr.id = dp.id_presentacion
            WHERE c.categoria = "Ropa niños"
            ORDER BY p.id ASC;

        """)
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_modamujer():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT p.id, p.nombre, p.precio, p.descuento, ROUND(p.precio - (p.precio * p.descuento), 2) AS precio_d, 
                p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
                p.enlace_imagen, pr.color
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id 
            INNER JOIN detalle_presentacion dp ON p.id = dp.id_producto
            INNER JOIN presentacion pr ON pr.id = dp.id_presentacion
            WHERE c.categoria = "Ropa Mujer"
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
            SELECT p.id, p.nombre, p.precio, p.descuento, p.descripcion, p.estado, tp.tipo AS tipo_producto, g.genero, m.marca, c.categoria, ge.grupoedad, 
            p.enlace_imagen
            FROM producto p 
            INNER JOIN tipo_producto tp ON p.id_tipo_producto = tp.id 
            INNER JOIN marca m ON p.id_marca = m.id 
            INNER JOIN categoria c ON p.id_categoria = c.id 
            INNER JOIN genero g ON p.id_genero = g.id 
            INNER JOIN grupo_edad ge ON p.id_grupo_edad = ge.id  where p.id= %s
        """, (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def produ():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
            select id,nombre, enlace_imagen from producto;
        """)
        productos = cursor.fetchall()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def actualizar_producto(id_producto, nombre, precio, estado, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, enlace_imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, estado = %s, descripcion = %s, descuento = %s, id_tipo_producto = %s, id_genero = %s, id_marca = %s, id_categoria = %s, id_grupo_edad = %s, enlace_imagen = %s WHERE id = %s",
                       (nombre, precio, estado, descripcion, descuento, id_tipo_producto, id_genero, id_marca, id_categoria, id_grupo_edad, enlace_imagen, id_producto))
    conexion.commit()
    conexion.close()

