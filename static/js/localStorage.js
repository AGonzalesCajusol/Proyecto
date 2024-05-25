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
function actualizar_storage(){
    var local = localStorage.getItem("productos");
    if (local) {
        var productos = JSON.parse(local);
        var id = 0
        var talla = ""
        var color = ""
        var precio = ""
        var cantidad = ""
        for (var i = 0; i < productos.length; i++){
            id = productos[i].id;
            talla = productos[i].talla;
            color = productos[i].color;
            cantidad = productos[i].cantidad;
            // consulta 1 es que exista stock
            //consulta 2 es que el  precio del producto se actualice
            //Paso 1
            

        }
    } else {
        console.log("No hay productos en el localStorage.");
    }
}