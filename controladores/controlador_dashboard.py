from bd import obtener_conexion

def cinco_productos_mas_vendidos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute('''select pr.nombre, sum(dp.subtotal) as subtotal  from producto pr inner join detalle_pedido dp
        on dp.id_producto = pr.id
        group by pr.nombre
        order by pr.nombre DESC
        LIMIT 5;''')
        productos = cursor.fetchall()
    conexion.close()
    return productos

