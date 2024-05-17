function cerrarVentanaCarrito() {
    var ventanaCarrito = document.getElementById("ventana-modal");
    ventanaCarrito.classList.remove("abrir");
    ventanaCarrito.classList.add("cerrar");

    setTimeout(function() {
        ventanaCarrito.style.display = 'none';
    },320);
    var botones = document.querySelectorAll('.btn-talla');
    botones.forEach(b => b.classList.remove('selected'));

    document.body.style.pointerEvents = "all";
    document.body.style.overflow = "visible";
    ventanaCarrito.style.pointerEvents = "all";
}

function cambiarColor(bttn) {
    var botones = document.querySelectorAll('.btn-talla');
    botones.forEach(b => b.classList.remove('selected'));
    bttn.classList.add('selected');
    bttn.setAttribute('id', 'btn-seleccionado');
}

function resetearIDboton(bttn) {
    bttn = document.querySelector('#btn-seleccionado').removeAttribute('id');
}

function abrirVentanaCarrito(boton) {

    var cardReferente = boton.closest('.card');

    var titulos = cardReferente.querySelector('.contenedor-titulo-card');
    var cantidades = cardReferente.querySelector('.cantidad-item');
    var precios = cardReferente.querySelector('.contenedor-precio h6:last-child');
    var imagen = cardReferente.querySelector('.item');

    var titulo = titulos.textContent.trim();
    var cantidad = cantidades.textContent.trim();
    var precio = precios.textContent.trim().replace('S/. ', '');
    var totalProducto = (cantidad * precio).toFixed(2);
    var rutaImagen = imagen.getAttribute('src');

    document.getElementById('valor-titulo-producto').textContent = titulo;
    document.getElementById('valor-precio').innerHTML = '<b>Precio: </b> S/. ' + precio;
    document.getElementById('valor-cantidad').innerHTML = '<b>Cantidad: </b>' + cantidad;
    document.getElementById('valor-total').innerHTML = '<b>Total: </b> S/. ' + totalProducto;
    document.getElementById('imagen-carrito-vista-previa').setAttribute('src', rutaImagen);

    mostrarVentanaCarrito();
}

function mostrarVentanaCarrito() {
    var ventanaCarrito = document.getElementById("ventana-modal");
    ventanaCarrito.classList.remove("cerrar");
    ventanaCarrito.classList.add("abrir");

    ventanaCarrito.style.display = 'flex';
    document.body.style.pointerEvents = "none";
    document.body.style.overflow = "hidden";
    ventanaCarrito.style.pointerEvents = "all";
}

// Event listener para detectar el final de la animación y eliminar la clase correspondiente de carrito de ventana modal 1
document.getElementById("ventana-modal").addEventListener("animationend", function() {
    this.classList.remove("abrir", "cerrar");
});



function abrirVentanaModal2() {
    var ventanaModal2 = document.getElementById("ventana-modal-2");
    ventanaModal2.classList.remove("cerrar");
    ventanaModal2.classList.add("abrir");
    console.log("Clase2 'abrir' agregada");
    ventanaModal2.style.display = 'flex';

    document.body.style.pointerEvents = "none";
    document.body.style.overflow = "hidden";
    ventanaModal2.style.pointerEvents = "all";
}

function cerrarVentanaModal2() {
    var ventanaModal2 = document.getElementById("ventana-modal-2");
    ventanaModal2.classList.remove("abrir");
    ventanaModal2.classList.add("cerrar");
    console.log("Clase2 'cerrar' agregada");
    setTimeout(function(){
        ventanaModal2.style.display = 'none';
    },320);

    document.body.style.pointerEvents = "all";
    document.body.style.overflow = "visible";
    ventanaModal2.style.pointerEvents = "all";
}

// Event listener para detectar el final de la animación y eliminar la clase correspondiente de carrito de ventana modal 1
document.getElementById("ventana-modal-2").addEventListener("animationend", function() {
    this.classList.remove("abrir", "cerrar");
});

function irCarrito() {
    var nuevaVentana = window.open('carrito_de_compras','_self');
}

/* //Variable global
var key = parseInt(1); */

function agregarProductoAlCarrito() {

    var botonSeleccionado = document.querySelector('#btn-seleccionado');

    if (botonSeleccionado !== null) {

        var valorTalla = botonSeleccionado.textContent;


        var titulo = document.getElementById('valor-titulo-producto').textContent;
        var rutaImagen = document.getElementById('imagen-carrito-vista-previa').getAttribute('src');
        var cantidad = parseInt(document.getElementById('valor-cantidad').textContent.replace('Cantidad: ', ''));
        
        var precioTexto = document.getElementById('valor-precio').textContent;
        var precio = precioTexto.valueOf();
        console.log("El precio es:", precio);
        
        var totalTexto = document.getElementById('valor-total').textContent;
        var total = totalTexto.valueOf();
        console.log("El total es:", total);
        
        var key = parseInt(obtenerValorUnico());
        
        var datos = {
            nombre: titulo,
            talla: valorTalla,
            rutaImagen: rutaImagen,
            cantidad: cantidad,
            precio: precio,
            subtotal: total
        };
        
        console.log(datos);
        
        localStorage.setItem(key, JSON.stringify(datos));

        cerrarVentanaCarrito();
        abrirVentanaModal2();
        resetearIDboton(botonSeleccionado);

    } else {
        alert("Seleccione una talla");
    }
}

function obtenerValorUnico() {
    // Obtén todas las claves del localStorage
    var claves = Object.keys(localStorage);

    // Filtra solo las claves que son numéricas
    var clavesNumericas = claves.filter(clave => !isNaN(clave));

    // Si no hay claves numéricas, el valor único es 1
    if (clavesNumericas.length === 0) {
        return 1;
    }

    // Convierte las claves a números y ordena de menor a mayor
    var numerosOrdenados = clavesNumericas.map(Number).sort((a, b) => a - b);

    // Compara cada número con su índice para encontrar el valor único
    for (var i = 0; i < numerosOrdenados.length; i++) {
        if (numerosOrdenados[i] !== i + 1) {
            return i + 1; // Encontró un hueco, devuelve el valor único
        }
    }

    // Si no se encontró ningún hueco, devuelve el siguiente valor
    return numerosOrdenados.length + 1;
}