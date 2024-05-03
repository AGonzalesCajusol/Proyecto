document.addEventListener("DOMContentLoaded", function() {
    var cards = document.querySelectorAll('.card');

    cards.forEach(function(card) {
        var btnMas = card.querySelector('.btn-mas');
        var btnMenos = card.querySelector('.btn-menos');
        var cantidadItem = card.querySelector('.cantidad-item');

        btnMas.addEventListener('click', function() {
            cantidadItem.textContent = parseInt(cantidadItem.textContent) + 1;
        });

        btnMenos.addEventListener('click', function() {
            if (parseInt(cantidadItem.textContent) > 1) {
                cantidadItem.textContent = parseInt(cantidadItem.textContent) - 1;
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var cards = document.querySelectorAll('.card');

    // Itera sobre cada card
    cards.forEach(function(card) {
        var btnMas = card.querySelector('.btn-mas');
        var btnMenos = card.querySelector('.btn-menos');
        var btnAgregar = card.querySelector('.btn-agregar-item');

        btnMas.addEventListener('click', function() {
            btnMas.classList.add('shrink');
            setTimeout(function() {
                btnMas.classList.remove('shrink');
            }, 200);
            
            cantidadItem.textContent = parseInt(cantidadItem.textContent) + 1;
        });

        btnMenos.addEventListener('click', function() {
            btnMenos.classList.add('shrink');
            setTimeout(function() {
                btnMenos.classList.remove('shrink');
            }, 200);

            if (parseInt(cantidadItem.textContent) > 1) {
                cantidadItem.textContent = parseInt(cantidadItem.textContent) - 1;
            }
        });

        btnAgregar.addEventListener('click', function() {
            btnAgregar.classList.add('shrink');
            setTimeout(function() {
                btnAgregar.classList.remove('shrink');
            }, 200);
        });
    });
});