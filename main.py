from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controladores.controlador_marca as controlador_marca, controladores.controlador_tipoproducto as controlador_tipoproducto, controladores.controlador_categoria as controlador_categoria, controladores.controlador_presentacion as controlador_presentacion, controladores.controlador_grupoedad as controlador_grupoedad, controladores.controlador_genero as controlador_genero, controladores.controlador_producto as controlador_producto, controladores.controlador_usuario as controlador_usuario
from clases import clase_categoria as clscat

app = Flask(__name__)
app.secret_key = 'secret'

#ruta para admi
@app.route('/')
@app.route('/usuario')
def usuario():
    return render_template('usuario_admin.html')

@app.route('/validarusuario', methods=['POST'])
def validarusuario():
    usuario = request.form['usuario']
    password = request.form['password']
    resullt = controlador_usuario.nombres_tipoproducto(usuario,password)
    if resullt:
        return redirect(url_for('ini'))
    else:
        flash('Datos incorrectos', 'success')
        return redirect(url_for('usuario'))
    

#------rutas de tienda



@app.route('/inicio')
def index():
    return render_template('/templates/index.html')

@app.route('/acerca_de')
def acerca_de():
    return render_template('/templates/acerca_de.html')

@app.route('/calzado')
def calzado():
    return render_template('/templates/calzado.html')

@app.route('/carrito_de_compras')
def carrito_de_compras():
    return render_template('/templates/carrito_de_compras.html')

@app.route('/libro_de_reclamaciones')
def libro_de_reclamaciones():
    return render_template('/templates/libro_de_reclamaciones.html')

@app.route('/moda_hombre')
def moda_hombre():
    return render_template('/templates/moda_hombre.html')

@app.route('/moda_mujer')
def moda_mujer():
    return render_template('/templates/moda_mujer.html')

@app.route('/moda_niños')
def moda_niños():
    return render_template('/templates/moda_niños.html')

@app.route('/pago_de_productos')
def pago_de_productos():
    return render_template('/templates/pago_de_productos.html')

@app.route('/preguntas_frecuentes')
def preguntas_frecuentes():
    return render_template('/templates/preguntas_frecuentes.html')

@app.route('/registro_de_usuario')
def registro_de_usuario():
    return render_template('/templates/registro_de_usuario.html')

@app.route('/ubicanos')
def ubicanos():
    return render_template('/templates/ubicanos.html')





#-------------------------
#-----------No tocar nada hacía abajo
#Puto el que modifica

@app.route('/ini')
def ini():
    return  render_template('maestra.html')

# --------marca--------------
@app.route('/marca')
def marca():
    marcas = controlador_marca.obtener_marcas()
    return render_template('marca.html', marcas=marcas)

@app.route('/registrarmarca')
def registrarmarca():
    return render_template('registrar_marca.html')

@app.route('/insertarmarca', methods=['POST'])
def insertar_marca():
    marca = request.form['marca']
    controlador_marca.insertar_marca(marca)
    return redirect('registrarmarca')

@app.route('/eliminarmarca/<int:id>')
def eliminar_marca(id):
    controlador_marca.eliminar_marca(id)
    return redirect(url_for('marca'))

@app.route('/modificarmarca', methods=['POST'])
def modificar_marca():
    id = request.form['id']
    marca = controlador_marca.obtener_marca_por_id(id)
    return render_template('modificar_marca.html', marca=marca)

@app.route('/actualizarmarca', methods=['POST'])
def actualizar_marca():
    id = request.form['id']
    marca = request.form['marca']
    controlador_marca.actualizar_marca(id,marca)
    return redirect('marca')

#---------tipo producto--------------

@app.route('/tipo_producto')
def tipo_producto():
    tipos_productos = controlador_tipoproducto.obtener_tipoproducto()
    return render_template('tipo_producto.html', tipos_productos = tipos_productos)

@app.route('/registrar_tipoproducto')
def registrar_tipoproducto():
    return render_template('registrar_tipoproducto.html')

@app.route('/insertar_tipoproducto', methods=['POST'])
def insertar_tipo_proucto():
    tipo = request.form['tipo']
    descripcion= request.form['descripcion']
    controlador_tipoproducto.insertar_tipoproducto(tipo,descripcion)
    return redirect('tipo_producto')

@app.route('/eliminar_tipoproducto/<int:id>')
def eliminar_tipoproducto(id):
    controlador_tipoproducto.eliminar_tipoproducto(id)
    return redirect(url_for('tipo_producto'))

@app.route('/modificar_tipoproducto', methods=['POST'])
def modificar_tipo_producto():
    id = request.form['id']
    tipo_producto = controlador_tipoproducto.obtener_tipoproducto_id(id)
    return render_template('modificar_tipoproducto.html', tipo_producto = tipo_producto)

@app.route('/actualizar_tipoproducto', methods=['POST'])
def actualizar_tipoproducto():
    id = request.form['id']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    controlador_tipoproducto.actualizar_tipoproducto(id,tipo,descripcion)
    return redirect('tipo_producto')

#------Categoria

@app.route('/categoria')
def categoria():
    categorias = controlador_categoria.obtener_categorias()
    return render_template('categoria.html', categorias=categorias)

@app.route('/registrar_categoria')
def registrar_categoria():
    return render_template('registrar_categoria.html')

@app.route('/insertar_categoria', methods=['POST'])
def insertar_categoria():
    categoria = request.form['categoria']
    controlador_categoria.insertar_categoria(categoria)
    return redirect(url_for('categoria'))

@app.route('/eliminar_categoria/<int:id>')
def eliminar_categoria(id):
    controlador_categoria.eliminar_categoria(id)
    return redirect(url_for('categoria'))

@app.route('/modificar_categoria', methods=['POST'])
def modificar_categoria():
    id = request.form['id']
    categoria = controlador_categoria.obtener_categoria_por_id(id)
    return render_template('modificar_categoria.html', categoria=categoria)

@app.route('/actualizar_categoria', methods=['POST'])
def actualizar_categoria():
    id = request.form['id']
    categoria = request.form['categoria']
    controlador_categoria.actualizar_categoria(id, categoria)
    return redirect(url_for('categoria'))

#--presentacion

@app.route('/presentacion')
def presentacion():
    presentaciones = controlador_presentacion.obtener_presentaciones()
    return render_template('presentacion.html', presentaciones=presentaciones)

@app.route('/registrar_presentacion')
def registrar_presentacion():
    return render_template('registrar_presentacion.html')

@app.route('/insertar_presentacion', methods=['POST'])
def insertar_presentacion():
    color = request.form['color']
    talla = request.form['talla']
    controlador_presentacion.insertar_presentacion(color, talla)
    return redirect(url_for('presentacion'))

@app.route('/eliminar_presentacion/<int:id>')
def eliminar_presentacion(id):
    controlador_presentacion.eliminar_presentacion(id)
    return redirect(url_for('presentacion'))

@app.route('/modificar_presentacion', methods=['POST'])
def modificar_presentacion():
    id = request.form['id']
    presentacion = controlador_presentacion.obtener_presentacion_por_id(id)
    return render_template('modificar_presentacion.html', presentacion=presentacion)

@app.route('/actualizar_presentacion', methods=['POST'])
def actualizar_presentacion():
    id = request.form['id']
    color = request.form['color']
    talla = request.form['talla']
    controlador_presentacion.actualizar_presentacion(id, color, talla)
    return redirect(url_for('presentacion'))

#----------grupoedad

@app.route('/grupo_edad')
def grupo_edad():
    grupos_edad = controlador_grupoedad.obtener_grupo_edad()
    return render_template('grupoedad.html', grupos_edad=grupos_edad)

@app.route('/registrargrupoedad')
def registrargrupoedad():
    return render_template('registrar_grupoedad.html')

@app.route('/insertar_grupo_edad', methods=['POST'])
def insertar_grupo_edad():
    grupo_edad = request.form['grupo_edad']
    controlador_grupoedad.insertar_grupo_edad(grupo_edad)
    return redirect(url_for('grupo_edad'))

@app.route('/eliminar_grupo_edad/<string:id>')
def eliminar_grupo_edad(id):
    controlador_grupoedad.eliminar_grupo_edad(id)
    return redirect(url_for('grupo_edad'))

@app.route('/modificar_grupoedad', methods=['POST'])
def modificar_grupo_edad():
    id = request.form['id']
    grupo_edad = controlador_grupoedad.obtener_grupo_edad_id(id)
    return render_template('modificar_grupoedad.html', grupo_edad=grupo_edad)

@app.route('/actualizar_grupo_edad', methods=['POST'])
def actualizar_grupo_edad():
    id = request.form['id']
    grupo_edad = request.form['grupo_edad']
    controlador_grupoedad.actualizar_grupo_edad(id, grupo_edad)
    return redirect(url_for('grupo_edad'))

#----Genero

@app.route('/genero')
def genero():
    generos = controlador_genero.obtener_generos()
    return render_template('genero.html', generos=generos)

@app.route('/registrargenero')
def registrargenero():
    return render_template('registrar_genero.html')

@app.route('/insertar_genero', methods=['POST'])
def insertar_genero():
    genero = request.form['genero']
    controlador_genero.insertar_genero(genero)
    return redirect(url_for('genero'))

@app.route('/eliminar_genero/<int:id>')
def eliminar_genero(id):
    controlador_genero.eliminar_genero(id)
    return redirect(url_for('genero'))

@app.route('/modificar_genero', methods=['POST'])
def modificar_genero():
    id = request.form['id']
    genero = controlador_genero.obtener_genero_por_id(id)
    return render_template('modificar_genero.html', genero=genero)

@app.route('/actualizar_genero', methods=['POST'])
def actualizar_genero():
    id = request.form['id']
    genero = request.form['genero']
    controlador_genero.actualizar_genero(id, genero)
    return redirect(url_for('genero'))

#----producto
@app.route('/producto')
def producto():
    productos = controlador_producto.obtener_productos()
    return render_template('producto.html', productos=productos)


@app.route('/registrarproducto')
def registrarproducto():
    datos = {
        'tipo_productos' : controlador_tipoproducto.nombres_tipoproducto(),
        'generos': controlador_genero.nombre_generos(),
        'marcas': controlador_marca.nombre_marcas(),
        'categorias': controlador_categoria.nombre_categorias(),
        'grupo_edad': controlador_grupoedad.nombres_grupo_edad(),
        'presentacion': controlador_presentacion.nombre_presentaciones()
    }
    return render_template('registrar_producto.html', **datos )

@app.route('/insertar_producto', methods=['POST'])
def insertar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    estado = request.form['estado']
    if estado == "Activo":
        estado = 'A'
    else:
        estado  = 'I'
    stock = request.form['stock']
    descripcion = request.form['descripcion']
    descuento = request.form['descuento']
    tipo_producto = request.form['tipo_producto']
    id_tipopr = controlador_tipoproducto.obtener_id_por_nombre(tipo_producto)  
    genero =request.form['genero']
    id_genero = controlador_genero.id_genero_por_nombre(genero)
    marca = request.form['marca']
    id_marca = controlador_marca.id_marca_por_nombre(marca)
    categoria = request.form['categoria']
    id_categoria = controlador_categoria.id_categoria_por_nombre(categoria)
    grupoedad = request.form['grupoedad']
    id_grupo_edad = controlador_grupoedad.id_grupo_edad_por_nombre(grupoedad)
    presentacion = request.form['presentacion']
    id_presentacion = controlador_presentacion.id_presentacion_por_nombre(presentacion)
    controlador_producto.insertar_producto(nombre,precio,estado,stock,descripcion,descuento,id_tipopr,id_genero,id_marca,id_categoria,id_grupo_edad,id_presentacion)
    return redirect(url_for('producto'))

@app.route('/modificar_producto', methods=['POST'])
def modificar_producto():
    id = request.form['id']
    datos = {
        'tipo_productos' : controlador_tipoproducto.nombres_tipoproducto(),
        'generos': controlador_genero.nombre_generos(),
        'marcas': controlador_marca.nombre_marcas(),
        'categorias': controlador_categoria.nombre_categorias(),
        'grupo_edad': controlador_grupoedad.nombres_grupo_edad(),
        'presentacion': controlador_presentacion.nombre_presentaciones()
    }
    pr = list(controlador_producto.obtener_producto_por_id(id))
    print(pr)
    return render_template('modifiar_producto.html', **datos, pr=pr)


@app.route('/actualizar_producto', methods=['POST'])
def actualizar_producto():
    id_producto = request.form['id']
    nombre = request.form['nombre']
    precio = request.form['precio']
    estado = request.form['estado']
    if estado == "Activo":
        estado = 'A'
    else:
        estado = 'I'
    stock = request.form['stock']
    descripcion = request.form['descripcion']
    descuento = request.form['descuento']
    tipo_producto = request.form['tipo_producto']
    id_tipopr = controlador_tipoproducto.obtener_id_por_nombre(tipo_producto)
    genero = request.form['genero']
    id_genero = controlador_genero.id_genero_por_nombre(genero)
    marca = request.form['marca']
    id_marca = controlador_marca.id_marca_por_nombre(marca)
    categoria = request.form['categoria']
    id_categoria = controlador_categoria.id_categoria_por_nombre(categoria)
    grupoedad = request.form['grupoedad']
    id_grupo_edad = controlador_grupoedad.id_grupo_edad_por_nombre(grupoedad)
    presentacion = request.form['presentacion']
    id_presentacion = controlador_presentacion.id_presentacion_por_nombre(presentacion)
    controlador_producto.actualizar_producto(id_producto, nombre, precio, estado, stock, descripcion, descuento, id_tipopr, id_genero, id_marca, id_categoria, id_grupo_edad, id_presentacion)
    return redirect(url_for('producto'))

@app.route('/apis_obtener_categorias')
def api_obtenercategorias():
    lista_categoria = controlador_categoria.obtener_categorias()
    rpt = dict()
    lista_c = []
    try:
        for categoria in lista_categoria:
            objCategoria =clscat.clsCategoria(categoria[0],categoria[1])
            lista_c.append(objCategoria.diccategoria)

        rpt["codigo"] = 1
        rpt["mensaje"]= "Procesamiento correcto"
        rpt["datos"] = lista_c
    except:
        rpt["codigo"]= 0
        rpt["mensaje"] = "Ocurrio un error"
        rpt["datos"] = list()
    return jsonify(rpt)


if __name__ ==  '__main__':
    app.run(debug=5000)