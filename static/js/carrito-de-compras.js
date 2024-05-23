// Se ejecuta al abrir la página
document.addEventListener("DOMContentLoaded", function () {
    var indicadorHayProductos = Object.keys(localStorage).filter(clave => !isNaN(clave)).length;
    if (indicadorHayProductos === 0) {
        mostrarDivNoHayProductos();
        document.getElementById("titulo-carrito-de-compras").remove();
    } else {
        mostrarDivHayProductos();
        cargarProductos();
    }
});

//Función que muestra los productos en el carrito de compras
function mostrarDivHayProductos() {
    var contenedorHayProductos = document.getElementById("contenedor-mostrar-hay-productos");
    var contenedorNoHayProductos = document.getElementById("contenedor-mostrar-no-hay-productos");
    contenedorHayProductos.style.display = "block";
    contenedorNoHayProductos.style.display = "none";
}

//Función que muestra una advertencia de que no hay productos agregados al carrito de compras
function mostrarDivNoHayProductos() {
    var contenedorHayProductos = document.getElementById("contenedor-mostrar-hay-productos");
    var contenedorNoHayProductos = document.getElementById("contenedor-mostrar-no-hay-productos");
    contenedorHayProductos.style.display = "none";
    contenedorNoHayProductos.style.display = "flex";
}


function cargarProductos() {
    // Obtener el div contenedor de productos
    var divContenedorProductos = document.getElementById("contenedor-productos");

    // Inicializar la cadena de registro
    var registro = '';

    // Recorrer el local storage para obtener todos los productos agregados
    for (var i = 0; i < localStorage.length; i++) {
        var clave = localStorage.key(i);

        if (clave !== "direccionCliente") {
            var itemClave = localStorage.getItem(clave);

            try {
                // Intentar analizar la cadena JSON
                var objetoProductoJSON = JSON.parse(itemClave);

                // Obtener los datos del producto
                var tituloProd = objetoProductoJSON.nombre;
                var tallaProd = objetoProductoJSON.talla;
                var rutaImagenProd = objetoProductoJSON.rutaImagen;
                var cantidadProd = objetoProductoJSON.cantidad;
                var precioProd = parseFloat(objetoProductoJSON.precio);
                var subtotalProd = parseFloat(objetoProductoJSON.subtotal);

                // Construir la representación HTML del producto
                registro += '<div class="card-producto"><div class="cont-producto"><p class="identificador-producto">' + clave + '</p><img class="img-card-producto" src="' + rutaImagenProd + '" alt=""><div class="cont-descr-producto"><h6 class="titulo-producto"><b>' + tituloProd + '</b></h6><h6><b>Talla: </b>' + tallaProd + '</h6><h6><b>Precio: </b>S/. ' + precioProd + '</h6><h6><b>Cantidad: </b>' + cantidadProd + '</h6><div><b>Subtotal producto: </b>S/. ' + subtotalProd + '</div></div><button id="btn-eliminar-producto" onclick="eliminarProductoDelCarrito()">Eliminar</button></div></div>';
            } catch (error) {
                // Manejar el error de JSON no válido
            }
        }
    }

    // Mostrar los productos en el contenedor
    divContenedorProductos.innerHTML = registro;
}

function guardardi (){
    var departamento = document.getElementById('cbobox-departamento').value;
    var provincia = document.getElementById('mostrar_provincias').value;
    var distrito = document.getElementById('distrito').value;
    var jiron = document.getElementById('text-avenida-calle-jiron').value;
    var direccion = document.getElementById("text-avenida-calle-jiron").value;
    var referencia = document.getElementById("text-dpto-int").value;
    console.log(departamento,provincia,distrito,jiron);
    try {
        if (departamento && provincia && distrito && jiron){
            localStorage.removeItem("datos_envio");
            var dic = {
                "departamento" : departamento,
                "provincia": provincia,
                "distrito": distrito,
                "jiron": jiron,
                "direccion": direccion,
                "referencia": referencia,
            }
            var dicJson = JSON.stringify(dic);
            localStorage.setItem('datos_envio', dicJson);
            window.open( "pago_de_productos");
        }else{
            alert("Ingrese todos sus datos porfavor")
        }
    } catch {
        alert("Ocurrio un error")
    }
}

//Función para eliminar un producto del carrito de compras
function eliminarProductoDelCarrito() {
    var identificadorProducto = event.target.parentElement.querySelector('.identificador-producto').innerText;

    // Elimina el producto del local storage
    localStorage.removeItem(identificadorProducto);

    // Actualiza la interfaz de usuario
    var indicadorHayProductos = Object.keys(localStorage).filter(clave => !isNaN(clave)).length;
    if (indicadorHayProductos === 0) {
        window.open("carrito_de_compras","_self");
    } else {
        cargarProductos();
    }
}
function guardarDatosCliente() {
    var valorCboBoxDep = document.getElementById("cbobox-departamento").value;
    var valorCboBoxProv = document.getElementById("cbobox-provincia").value;
    var valorCboBoxDist = document.getElementById("cbobox-distrito").value;
    var valorCalle = document.getElementById("text-avenida-calle-jiron").value;
    var valorDptoOpcional = document.getElementById("text-dpto-int").value;

    var keyDireccion = 'direccionCliente';

    var datosDireccion ={
        dpto: valorCboBoxDep,
        prov: valorCboBoxProv,
        dist: valorCboBoxDist,
        calle: valorCalle,
        depapisoetc: valorDptoOpcional
    };

    localStorage.setItem(keyDireccion,JSON.stringify(datosDireccion));
}


async function mostrar_provincias(){
    var departamento = document.getElementById('cbobox-departamento').value; 
    try {
        if (departamento){
        const response = await fetch(`/retornar_provincias/${departamento}`);
        const data = await response.json();
        var select = document.getElementById("mostrar_provincias");
        select.innerHTML = "";
        for (var i = 0 ;  i< data.length ;  i++){
            var option = document.createElement("option");
            option.value = data[i];
            option.textContent = data[i];
            select.appendChild(option);
        }
        }
    } catch (error) {
        console.error('Error al obtener los datos de provincia:', error);
    }
}

async function mostrar_distritos() {
    var provincia = document.getElementById('mostrar_provincias').value; // Obtener el valor seleccionado de la provincia
    try {
        if (provincia) {
            const response = await fetch(`/retornar_distritos/${provincia}`);
            const data = await response.json();
            var select = document.getElementById("distrito");
            select.innerHTML = "";
            for (var i = 0 ;  i< data.length ;  i++){
                var option = document.createElement("option");
                option.textContent = data[i];
                select.appendChild(option);
            }
        }
    } catch (error) {
        console.error('Error al obtener los datos de distritos:', error);
    }
}

function agregarProductoAlCarrito() {
    var botonSeleccionado = document.querySelector('#btn-seleccionado');

    if (botonSeleccionado !== null) {


        var titulo = document.getElementById('valor-titulo-producto').textContent;
        var rutaImagen = document.getElementById('imagen-carrito-vista-previa').getAttribute('src');
        var cantidad = parseInt(document.getElementById('valor-cantidad').textContent.replace('Cantidad: ', ''));
        
        var precio = document.getElementById('valor-precio').textContent;
        var precio = parseFloat(precio.match(/\d+\.\d+/)[0]).toFixed(2);

        var total = document.getElementById('valor-total').textContent;
        total =parseFloat(total.match(/\d+\.\d+/)[0]).toFixed(2);
  
        
        var key = parseInt(obtenerValorUnico());
        
        var datos = {   
            // id: elid,
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

