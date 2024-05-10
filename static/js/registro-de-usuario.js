$(document).ready(function (){
    $('#dni').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue) || inputValue.length > 8) {
            $(this).val(inputValue.slice(0, 8).replace(/[^0-9+]/g, ''));
        }
    });

    $('#contraseña').on('input', function () {
        var inputValue = $(this).val();
        if (/[^0-9+]/.test(inputValue)) {
            $(this).val(inputValue.replace(/[*]/g, ''));
        }
    });
});