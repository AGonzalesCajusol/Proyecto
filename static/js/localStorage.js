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
        for (var i = 0; i < productos.length; i++) {
            var id = productos[i].id;
            var talla = productos[i].talla;
            var color = productos[i].color;
            
            var xml = new XMLHttpRequest();
            var url = "/retornar_stockproducto/"+ id+ "/"+color + "/"+ talla;
            xml.open("GET", url, true); // Cambiado a método GET
            xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xml.onload = function() {
                if (xml.status >= 200 && xml.status < 300) {
                    console.log("Stock actualizado:", xml.responseText);
                } else {
                    console.log("No hay productos", xml.responseText);
                }
            };
            xml.onerror = function() {
                console.error('Error en la solicitud XMLHttpRequest');
            };
            xml.send();
        }
    } else {
        console.log("No hay productos en el localStorage.");
    }
}
