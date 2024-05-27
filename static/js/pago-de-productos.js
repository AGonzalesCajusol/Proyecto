var subtotales = 0
var costoEnvio = 0
var tota = 0
document.addEventListener("DOMContentLoaded", function () {
    document.body.style.opacity = "1";
    cargarProductos();
    var inputEnfocarPorDefecto = document.getElementById("num1").focus();
});

function cargarProductos() {
    validar_stock();
    // Obtengo los divs donde se insertarán los productos y los precios
    var divContenedorProductos = document.getElementById("productos");
    var divContenedorPrecios = document.getElementById("precios");

    // Variables para almacenar el contenido HTML de los productos y los precios
    var registroProductos = '';
    var registroPrecios = '';
    var total = 0;
    costoEnvio = document.getElementById('mnt').value;

    var local = JSON.parse(localStorage.getItem("productos"));
    var datosEnvio = JSON.parse(localStorage.getItem("datos_envio"));
    var direccion = " departamento " + datosEnvio.departamento + " provincia  " + datosEnvio.provincia + "distrito " + datosEnvio.distrito + "Jirón: " + datosEnvio.jiron
    for (var i = 0; i < local.length; i++) {
        var objPr = local[i];
        var tituloProd = objPr.nombre;
        var tallaProd = objPr.talla;
        var rutaImagenProd = objPr.rutaImagen;
        var cantidadProd = objPr.cantidad;
        var precioProd = parseFloat(objPr.precio);
        var subtotalProd = parseFloat(objPr.subtotal);
        registroProductos += '<div class="card-producto"><div class="cont-producto"><img class="img-card-producto" src="' + rutaImagenProd + '" alt=""><div class="cont-descr-producto"><h6 class="titulo-producto"><b>' + tituloProd + '</b></h6><h6><b>Talla: </b>' + tallaProd + '</h6><h6><b>Precio: </b>S/. ' + precioProd + '</h6><h6><b>Cantidad: </b>' + cantidadProd + '</h6><div><b>Subtotal producto: </b>S/. ' + subtotalProd + '</div></div></div></div>';
    }
    subtotal();
    totalAPagar = parseFloat(subtotales) + parseFloat(costoEnvio);
    registroPrecios += '<div class="subtotal-costo-envio-total"><h6><b>Subtotal productos: </b></h6><h6>S/. ' + subtotales + '</h6></div><div class="subtotal-costo-envio-total"><h6><b>Costo de envío: </b></h6><h6>S/. ' + parseFloat(costoEnvio).toFixed(2) + '</h6></div><div class="subtotal-costo-envio-total"><h6><b>Total a pagar: </b></h6><h6>S/. ' + totalAPagar + '</h6></div><div class="envio"><h6><b>Sera enviado a la dirección: </b></h6><h6>' + direccion + '</h6></div>';
    divContenedorProductos.innerHTML = registroProductos;
    divContenedorPrecios.innerHTML = registroPrecios;
}

function subtotal() {
    var local = JSON.parse(localStorage.getItem("productos"));
    for (var i = 0; i < local.length; i++) {
        var objPr = local[i];
        subtotales += objPr.subtotal;
    }
}

function mostrarResumenPedido() {
    var numtarj1 = document.getElementById("num1").value;
    var numtarj2 = document.getElementById("num2").value;
    var numtarj3 = document.getElementById("num3").value;
    var numtarj4 = document.getElementById("num4").value;
    var fectarj1 = document.getElementById("fec1").value;
    var fectarj2 = document.getElementById("fec2").value;
    var cvvtarj = document.getElementById("cvv").value;
    if (numtarj1.trim() === '' || numtarj2.trim() === '' || numtarj3.trim() === '' || numtarj4.trim() === '' || fectarj1.trim() === '' || fectarj2.trim() === '' || cvvtarj.trim() === '') {
        alert("Por favor, ingrese sus datos para continuar");
    } else {
        mostrarValoresDireccionCliente();
        document.getElementById("contenedor-mostrar-hay-productos").style.display = "flex";
    }
    var datosLocalStorage = JSON.stringify(localStorage.getItem('direccionCliente'));
    document.getElementById('datosLocalStorageInput').value = datosLocalStorage;
    document.getElementById('formularioDatosLocalStorage').submit();
}

//Setear los campos de dirección ingresada
function mostrarValoresDireccionCliente() {
    var numTarj1 = document.getElementById("num1").value;
    var numTarj2 = document.getElementById("num2").value;
    var numTarj3 = document.getElementById("num3").value;
    var numTarj4 = document.getElementById("num4").value;

    var claveDireccion = localStorage.getItem("direccionCliente");

    if (claveDireccion) {
        var objetoJSON = JSON.parse(claveDireccion);
        var valCalle = objetoJSON.calle;
        var valPisoOpc = objetoJSON.depapisoetc;
        var valDepart = formatoTitulo(objetoJSON.dpto);
        var valProv = formatoTitulo(objetoJSON.prov);
        var valDist = formatoTitulo(objetoJSON.dist);


        // Resto del código para utilizar los valores obtenidos...
    } else {
        console.log("La clave 'direccionCliente' no existe en localStorage.");
    }

    var contenedorDireccion = document.getElementById("contenedor-direccion-envio");
    var contenedorTarjeta = document.getElementById("contenedor-tarjeta");

    if (!valPisoOpc || valPisoOpc.trim() === "") {
        contenedorDireccion.innerHTML = '<h6><b>Dirección de entrega: </b>' + valCalle + ', ' + valDist + ', ' + valProv + ', ' + valDepart + '</h6>';
    } else {
        contenedorDireccion.innerHTML = '<h6><b>Dirección de entrega: </b>' + valCalle + ', ' + valPisoOpc + ', ' + valDist + ', ' + valProv + ', ' + valDepart + '</h6>';
        contenedorTarjeta.innerHTML = '<h6><b>Tarjeta: </b></h6><h6>VISA N° ' + numTarj1 + ' - ' + numTarj2 + ' - ' + numTarj3 + ' - ' + numTarj4 + '</h6>';
    }
}


// Función para convertir a formato de título
function formatoTitulo(cadena) {
    return cadena.charAt(0).toUpperCase() + cadena.slice(1).toLowerCase();
}


//Cambiar color de los botones
function cambiarColor(botonClicado) {
    var botones = document.getElementsByClassName("btn-medio-pago");
    for (var i = 0; i < botones.length; i++) {
        botones[i].style.backgroundColor = "#ebebeb";
    }
    botonClicado.style.backgroundColor = "#917c04";
}

//Validar checkboxs
function manejarCheckbox(checkboxClicado) {
    var checkboxes = document.querySelectorAll('.form-check-input');

    // Desmarcar todos los checkboxes
    checkboxes.forEach(function (checkbox) {
        if (checkbox !== checkboxClicado) {
            checkbox.checked = false;
        }
    });
}


//Validar campos de números, fechas y cvv de tarjeta
$(document).ready(function () {
    $('#num1').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 4) {
            $(this).val(inputValue.slice(0, 4).replace(/[^0-9+]/g, ''));
        }
    });

    $('#num2').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 4) {
            $(this).val(inputValue.slice(0, 4).replace(/[^0-9+]/g, ''));
        }
    });

    $('#num3').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 4) {
            $(this).val(inputValue.slice(0, 4).replace(/[^0-9+]/g, ''));
        }
    });

    $('#num4').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 4) {
            $(this).val(inputValue.slice(0, 4).replace(/[^0-9+]/g, ''));
        }
    });

    $('#fec1').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 2) {
            $(this).val(inputValue.slice(0, 2).replace(/[^0-9+]/g, ''));
        }
    });

    $('#fec2').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 2) {
            $(this).val(inputValue.slice(0, 2).replace(/[^0-9+]/g, ''));
        }
    });

    $('#cvv').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 3) {
            $(this).val(inputValue.slice(0, 3).replace(/[^0-9+]/g, ''));
        }
    });

    $('#input-dni-cliente-pago').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 8) {
            $(this).val(inputValue.slice(0, 8).replace(/[^0-9+]/g, ''));
        }
    });
});

//Función para cerrar la ventana de pago realizado (limpia todos los items que se hayan comprado)
function cerrarVentanaPagoRealizado() {
    var ventanaPagoRealizado = document.getElementById("cont-pago-realizado");
    ventanaPagoRealizado.style.display = "none";
    localStorage.clear();
}

//Función para ir a la página de inicio(también limpiar los items en el local storage)
function irPaginaDeInicio() {
    window.open("index-html");
    localStorage.clear();
}

function abrirVentanaModalPagoConfirmado() {
    var dniReceptorPedido = document.getElementById("input-dni-cliente-pago").value;
    var nomApeReceptorPedido = document.getElementById("input-dni-nomApe-cliente").value;
    var mensaje = document.getElementById("mensaje");
    var elemento = document.getElementById("sta");
    var imgElement = document.getElementById("im");

    if (dniReceptorPedido.length === 0 || nomApeReceptorPedido.length === 0) {
        alert("LLena los campos del receptor");
    } else {
        const datosReceptor = {
            dni: dniReceptorPedido,
            nombre: nomApeReceptorPedido
        };    
        const datosEnvio = JSON.parse(localStorage.getItem('datos_envio'));
        const productos = JSON.parse(localStorage.getItem('productos'));
        const data = {
            datos_envio: datosEnvio,
            productos: productos,
            datos_receptor: datosReceptor
        };  
        const mensaje = true
        fetch('/transaccion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Transacción completada con éxito:', data.message);
            } else {
                mensaje = data.message;
            }
        })
        .catch(error => {
            console.error('Error al realizar la solicitud:', error);
            mensaje = false
        });
        
        document.getElementById("message").click();
        var enlace = document.getElementById("enlace");
        function actionAfterThreeSeconds() {
            mensaje.textContent = "";
            elemento.remove();
            if (dniReceptorPedido && nomApeReceptorPedido && mensaje) {
                mensaje.textContent = "Felicidades por su compra";
                enlace.href = "/inicio";
                enlace.textContent = "Ir";
                var imagePath = "/static/img/check.gif";
            } else {
                mensaje.textContent = "La transacción ha sido fallida";
                var imagePath = "/static/img/cnacelar.gif";
                enlace.textContent = "X";
                enlace.href = "carrito_de_compras";
            }
            imgElement.src = imagePath;
        }
        setTimeout(actionAfterThreeSeconds, 3000);
    }
}
//limpiar local
//Pasar de un campo a otro sin necesidad de hacer tab o click en él
function checkInput(input, nextInputID) {
    var inputValueLength = input.value.length;
    if (inputValueLength === input.maxLength) {
        var nextInput = document.getElementById(nextInputID);
        if (nextInput) {
            nextInput.focus();
        }
    }
}
function habilitar(idCheckbox) {
    var chckboxRecibireYo = document.getElementById("chckbox-recibire-yo");
    var chckboxRecibiraOtro = document.getElementById("chckbox-recibira-otra-persona");
    var dniReceptorPedido = document.getElementById("input-dni-cliente-pago");
    var nomApeReceptorPedido = document.getElementById("input-dni-nomApe-cliente");

    if (idCheckbox === "chckbox-recibire-yo" && chckboxRecibireYo.checked) {
        chckboxRecibiraOtro.checked = false;
    } else if (idCheckbox === "chckbox-recibira-otra-persona" && chckboxRecibiraOtro.checked) {
        chckboxRecibireYo.checked = false;
    }

    if (chckboxRecibireYo.checked || chckboxRecibiraOtro.checked) {
        dniReceptorPedido.disabled = false;
        nomApeReceptorPedido.disabled = false;
    } else {
        dniReceptorPedido.disabled = true;
        nomApeReceptorPedido.disabled = true;
    }
}


