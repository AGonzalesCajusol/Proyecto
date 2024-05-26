window.onload = function() {
    var pathname = window.location.pathname;
    if (pathname === "/carrito_de_compras") {
        actualizar_storage();
    } else if (pathname === "/pagina2.html") {
        otra_funcion();
    } else {
        console.log("No hay una función específica para esta página.");
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

function actualizar_storage() {
    obtener_datos().then(function(datos) {
        var stocks = datos[0];
        var precios = datos[1];

        //validamos el stock de cada producto 
        var productos = localStorage.getItem("productos")
        var objPr = JSON.parse(productos);
  
        for (var i = 0 ; i< objPr.length; i++){
            var producto =  objPr[i]
            var stock = producto.cantidad;
            console.log(stocks[i])
            console.log(stock)
        }


    }).catch(function(error) {
        console.error("Error al actualizar los datos:", error);
    });
}

