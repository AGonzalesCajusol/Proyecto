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
function actualizar_storage() {
    var local = localStorage.getItem("productos");
    if (local) {
        var productos = JSON.parse(local);
        var promesas = productos.map(function(producto, index) { // Guarda el índice original de cada producto
            return new Promise(function(resolve, reject) {
                var xml = new XMLHttpRequest();
                var url = "/retornar_stockproducto/" + producto.id + "/" + producto.color + "/" + producto.talla;
                xml.open("GET", url, true);
                xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xml.onload = function() {
                    if (xml.status >= 200 && xml.status < 300) {
                        const xmlResponseText = xml.responseText; 
                        const valores = xmlResponseText.split('<valor>').slice(1).map(cadena => cadena.split('</valor>')[0].trim());
                        const numeros = valores.map(valor => {
                            const valorLimpio = valor.replace(/[^\d.]/g, '').trim();
                            return parseFloat(valorLimpio);
                        });
                        resolve({ index: index, numeros: numeros }); 
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
            const numerosOrdenados = resultados.map(resultado => resultado.numeros);
            console.log("Datos actualizados:", numerosOrdenados);
        }).catch(function(error) {
            console.error("Error al actualizar los datos:", error);
        });
    } else {
        console.log("No hay productos en el localStorage.");
    }
}
