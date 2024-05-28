var estado = false;
var toti = 0
actualizar_productos();
window.onload = function() {
    var pre = document.getElementById("total");
    var pathname = window.location.pathname;
    document.getElementById("miFormulario").style.display = "none";
    subtotal();
    var pre = document.getElementById("total");
    if (pathname === "/carrito_de_compras") {
        actualizar_productos();
        validar_stock();
        pre.textContent = toti;
    } else if (pathname === "/pago_deproducto") {
        actualizar_productos();
    } 
};

function obtener_datos() {
    return new Promise(function(resolve, reject) {
        var local = localStorage.getItem("productos");
        if (local) {
            var productos = JSON.parse(local);
            var promesas = productos.map(function(producto, index) {
                return new Promise(function(resolve, reject) {
                    var xml = new XMLHttpRequest();
                    var url = "/retornar_stockproducto/" + producto.id + "/" + producto.color + "/" + producto.talla;
                    xml.open("GET", url, true);
                    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    xml.onload = function() {
                        if (xml.status >= 200 && xml.status < 300) {
                            const parser = new DOMParser();
                            const xmlDoc = parser.parseFromString(xml.responseText, "text/xml");
                            const stock = parseFloat(xmlDoc.getElementsByTagName("stock")[0].childNodes[0].nodeValue);
                            const precio = parseFloat(xmlDoc.getElementsByTagName("precio")[0].childNodes[0].nodeValue);
                            resolve({ index: index, stock: stock, precio: precio });
                        } else {
                            reject("No hay productos");
                        }
                    };
                    xml.onerror = function() {
                        reject('Error en la solicitud XMLHttpRequest');
                    };
                    xml.send();
                });
            });

            Promise.all(promesas).then(function(resultados) {
                resultados.sort((a, b) => a.index - b.index);
                const stocks = resultados.map(resultado => resultado.stock);
                const precios = resultados.map(resultado => resultado.precio);
                resolve([stocks, precios]);
            }).catch(function(error) {
                reject(error);
            });
        } else {
            reject("No hay productos en el localStorage.");
        }
    });
}

function actualizar_productos() {
    obtener_datos().then(function(datos) {
        var precios = datos[1];
        var productos = localStorage.getItem("productos");
        var objPr = JSON.parse(productos);
        var pr = [];

        for (var i = 0; i < objPr.length; i++) {
            var producto = objPr[i];
            var subtotal = producto.cantidad * precios[i];
            var diccionario = {
                "cantidad": producto.cantidad,
                "color": producto.color,
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": precios[i],
                "rutaImagen": producto.rutaImagen,
                "subtotal": subtotal,
                "talla": producto.talla
            };
            pr.push(diccionario);
        }
        localStorage.setItem("productos", JSON.stringify(pr));
    }).catch(function(error) {
        console.error("Error al actualizar los datos:", error);
    });
}

function validar_stock() {
    obtener_datos().then(function(datos) {
        estado = true;
        var stocks = datos[0];
        var precios = datos[1];
        var productos = localStorage.getItem("productos");
        var objPr = JSON.parse(productos);
        var docu = document.getElementsByClassName('card-producto');

        for (var i = 0; i < objPr.length; i++) {
            var stock = objPr[i].cantidad;
            var id = "stockDiv_" + i; 
            var existingDiv = document.getElementById(id);

            console.log(stocks[i])

            if (stock >= stocks[i]) {
                if (stocks[i] == 0) {
                    if (!existingDiv) {
                        var div = document.createElement("div");
                        div.id = id;
                        div.textContent = "No hay stock del producto";
                        docu[i].classList.add("border", "border-danger", "border-3");
                        docu[i].appendChild(div);
                    } else {
                        existingDiv.textContent = "No hay stock del producto";
                    }
                    estado = false;
                } else {
                    if (!existingDiv) {
                        var div = document.createElement("div");
                        div.id = id;
                        div.textContent = "Del producto solo quedan " + stocks[i] + " productos";
                        docu[i].classList.add("border", "border-danger", "border-3");
                        docu[i].appendChild(div);
                    } else {
                        existingDiv.textContent = "Del producto solo quedan " + stocks[i] + " productos";
                    }
                    estado = false;
                }
                alert("Verifica el stock" + objPr[1].nombre);
            } else {
                if (existingDiv) {
                    docu[i].removeChild(existingDiv);
                }
            }

        }
        return estado;
    }).catch(function(error) {
        console.error("Error al actualizar los datos:", error);
    });
}
function subtotal() {
    var local = JSON.parse(localStorage.getItem("productos"));
    for (var i = 0; i < local.length; i++) {
        var objPr = local[i];
        toti += objPr.subtotal;
    }
}

function guardardi() {
    var departamento = document.getElementById('cbobox-departamento').value;
    var provincia = document.getElementById('mostrar_provincias').value;
    var distrito = document.getElementById('distrito').value;
    var jiron = document.getElementById('text-avenida-calle-jiron').value;
    var direccion = document.getElementById("text-avenida-calle-jiron").value;
    var referencia = document.getElementById("text-dpto-int").value;
    var esta = true;
    try {
        validar_stock();
        if (departamento && provincia && distrito && jiron) {
            localStorage.removeItem("datos_envio");
            var dic = {
                "departamento": departamento,
                "provincia": provincia,
                "distrito": distrito,
                "jiron": jiron,
                "direccion": direccion,
                "referencia": referencia,
                "monto": 0.0
            }
            var dicJson = JSON.stringify(dic);
            localStorage.setItem('datos_envio', dicJson);
        } else {
            alert("Ingrese todos sus datos por favor");
            esta = false;
        }
       if (esta && estado) {
            // Llenar los campos del formulario con los valores adecuados
            document.getElementsByName('distri')[0].value = distrito;
            document.getElementsByName('provi')[0].value = provincia;
            document.getElementsByName('depa')[0].value = departamento;

            // Obtener el botón de enviar del formulario
            var botonEnviar = document.getElementById('enviar');

            // Hacer clic en el botón de enviar
            botonEnviar.click();
       }
       
    } catch (error) {
        alert("Ocurrió un error: " + error);
    }
}
