function mostrarMenuLateral() {
    var containerMenu = document.querySelector('.container-menu');
    var body = document.body;

    if (containerMenu.style.visibility === 'visible' && containerMenu.style.transform === 'translateX(0%)') {
        containerMenu.style.visibility = 'hidden';
        containerMenu.style.transform = 'translateX(-100%)';
        body.classList.remove('menu-open');
        body.style.overflow='auto';
    } else {
        containerMenu.style.visibility = 'visible';
        containerMenu.style.transform = 'translateX(0%)';
        body.classList.add('menu-open');
        body.style.overflow = 'auto';
    }
}


function abrirVentanaModalInicioDeSesion() {
    var ventanaIncioSesion = document.getElementById("ventana-modal-inicio-sesion");
    ventanaIncioSesion.style.display="flex";
    setTimeout(function () {
        ventanaIncioSesion.classList.add("mostrar");
    }, 10);
    document.body.style.pointerEvents="none";
    document.body.style.overflow="hidden";
    ventanaIncioSesion.style.pointerEvents="all";
}

function cerrarVentanaModalInicioSesion() {
    var ventanaIncioSesion = document.getElementById("ventana-modal-inicio-sesion");
    ventanaIncioSesion.classList.remove("mostrar");
    setTimeout(function () {
        ventanaIncioSesion.style.display = "none";
    }, 500);
    document.body.style.pointerEvents="all";
    document.body.style.overflow="visible";
    ventanaIncioSesion.style.pointerEvents="all";
}

function abrirPaginaRegistroDeUsuario() {
    window.open('registro_de_usuario.html','_blank');
}



