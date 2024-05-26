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
        var promesas = productos.map(function(producto) {
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
                            // Reemplaza cualquier carácter que no sea un dígito o un punto con un espacio en blanco y luego elimina espacios en blanco adicionales
                            const valorLimpio = valor.replace(/[^\d.]/g, '').trim();
                            return parseFloat(valorLimpio);
                        });
                        console.log(numeros);
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

        Promise.all(promesas).then(function(datos) {
            console.log("Datos actualizados:", datos);
            // Guardar 'datos' en localStorage o realizar alguna otra acción
            localStorage.setItem("datos_actualizados", JSON.stringify(datos));
        }).catch(function(error) {
            console.error("Error al actualizar los datos:", error);
        });
    } else {
        console.log("No hay productos en el localStorage.");
    }
}
