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
    //Obtengo el div al que le insertaré el producto
    var divContenedorProductos = document.getElementById("contenedor-productos");

    //Variable para almacenar el contenido HTML del div al que le insertaré los productos
    var registro = '';

    //Recorro el local storage para obtener todos los productos agregados
    for (i = 0; i < localStorage.length; i++) {
        //Obtengo el producto almacenado en el local sotrage
        var clave = localStorage.key(i);

        if (clave !== "direccionCliente"){
            var itemClave = localStorage.getItem(clave);
        var objetoProductoJSON = JSON.parse(itemClave);

        //Obtengo los datos del producto
        var tituloProd = objetoProductoJSON.nombre;
        var tallaProd = objetoProductoJSON.talla;
        var rutaImagenProd = objetoProductoJSON.rutaImagen;
        var cantidadProd = objetoProductoJSON.cantidad;
        var precioProd = parseFloat(objetoProductoJSON.precio);
        var subtotalProd = parseFloat(objetoProductoJSON.subtotal);

        registro += '<div class="card-producto"><div class="cont-producto"><p class="identificador-producto">'+ clave +'</p><img class="img-card-producto" src="' + rutaImagenProd + '" alt=""><div class="cont-descr-producto"><h6 class="titulo-producto"><b>' + tituloProd + '</b></h6><h6><b>Talla: </b>' + tallaProd + '</h6><h6><b>Precio: </b>S/. ' + precioProd + '</h6><h6><b>Cantidad: </b>' + cantidadProd + '</h6><div><b>Subtotal producto: </b>S/. ' + subtotalProd + '</div></div><button id="btn-eliminar-producto" onclick="eliminarProductoDelCarrito()">Eliminar</button></div></div>';
        }
    }
    
    var cantidadProductos=0;

    for (let i = 0; i < localStorage.length; i++) {
        var key = localStorage.key(i);
        if (key !== "direccionCliente") {
            cantidadProductos++;
        }
    }

    if (cantidadProductos>1) {
        divContenedorProductos.innerHTML = registro + '<div class="cont-editar-pedido--tienes-n-productos"><label id="lbl-tienes-n-prod" for=""><i>Tienes <b><u>' + cantidadProductos + ' productos</u></b></i></label></div>';
    } else {
        divContenedorProductos.innerHTML = registro + '<div class="cont-editar-pedido--tienes-n-productos"><label id="lbl-tienes-n-prod" for=""><i>Tienes <b><u>' + cantidadProductos + ' producto</u></b></i></label></div>';
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
        window.open("carrito_de_compras.html","_self");
    } else {
        cargarProductos();
    }
}


function irPaginaPagoDeProductos() {
    var valorCboBoxDep = document.getElementById("cbobox-departamento").value;
    var valorCboBoxProv = document.getElementById("cbobox-provincia").value;
    var valorCboBoxDist = document.getElementById("cbobox-distrito").value;
    var valorDireccion = document.getElementById("text-avenida-calle-jiron").value;

    if (
        valorCboBoxDep.trim() === "" ||
        valorCboBoxProv.trim() === "" ||
        valorCboBoxDist.trim() === "" ||
        valorDireccion.trim() === ""
      ) {
        alert("Por favor, ingrese una dirección válida");
      } else {
        guardarDatosCliente();
        window.open("pago_de_productos.html","_self");
      }
}

//Función para obtener los datos de la dirección del cliente
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


//Agregar provincias dependiendo el departamento seleccionado
function actualizarProvincias() {
    var departamentoSeleccionado = document.getElementById("cbobox-departamento").value;

    var comboProvincias = document.getElementById("cbobox-provincia");

    comboProvincias.innerHTML = '';

    if (departamentoSeleccionado === "lambayeque") {
        agregarOpcionProvincias(comboProvincias, "chiclayo", "Chiclayo");
    } else if (departamentoSeleccionado === "lima") {
        agregarOpcionProvincias(comboProvincias, "lima", "Lima");
    }
    actualizarDistritos();
}

function agregarOpcionProvincias(selectElement, value, text) {
    var opcion = document.createElement("option");
    opcion.value = value;
    opcion.text = text;
    selectElement.add(opcion);
}


//Agregar distritos dependiendo la pronvincia seleccionada
function actualizarDistritos() {
    var provinciaSeleccionada = document.getElementById("cbobox-provincia").value;

    var comboDistritos = document.getElementById("cbobox-distrito");

    comboDistritos.innerHTML = '';

    if (provinciaSeleccionada === "chiclayo") {
        agregarOpcionDistritos(comboDistritos, "pimentel", "Pimentel");
        agregarOpcionDistritos(comboDistritos, "lagunas", "Lagunas");
        agregarOpcionDistritos(comboDistritos, "monsefu", "Monsefú");
        agregarOpcionDistritos(comboDistritos, "eten", "Eten");
        agregarOpcionDistritos(comboDistritos, "puertoeten", "Puerto Eten");
        agregarOpcionDistritos(comboDistritos, "cayaltí", "Cayaltí");
        agregarOpcionDistritos(comboDistritos, "chiclayo", "Chiclayo");
        agregarOpcionDistritos(comboDistritos, "la victoria", "La Victoria");
    } else if (provinciaSeleccionada === "lima") {
        agregarOpcionDistritos(comboDistritos, "breña", "Breña");
        agregarOpcionDistritos(comboDistritos, "sanisidro", "San Isidro");
        agregarOpcionDistritos(comboDistritos, "lamolina", "La Molina");
        agregarOpcionDistritos(comboDistritos, "santiagodesurco", "Santiago de Surco");
        agregarOpcionDistritos(comboDistritos, "lince", "Lince");
        agregarOpcionDistritos(comboDistritos, "surquillo", "Surquillo");
        agregarOpcionDistritos(comboDistritos, "chosica", "Chosica");
        agregarOpcionDistritos(comboDistritos, "comas", "Comas");
    }
}

function agregarOpcionDistritos(selectElement, value, text) {
    var opcion = document.createElement("option");
    opcion.value = value;
    opcion.text = text;
    selectElement.add(opcion);
}