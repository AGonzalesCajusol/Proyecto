document.addEventListener('DOMContentLoaded', function () {
  var formulario = document.querySelector('form');

  formulario.addEventListener('submit', function (event) {
    event.preventDefault();

    if (validarFormulario()) {
      enviarFormulario();
    }
  });

  function validarFormulario() {
    var numeroDocumento = document.getElementById('numero-documento').value;
    var correo = document.getElementById('correo').value;
    var monto = document.getElementById('monto').value;

    if (!validarNumeroDocumento(numeroDocumento)) {
      alert('Por favor, ingrese un número de documento válido.');
      return false;
    }

    if (!validarCorreo(correo)) {
      alert('Por favor, ingrese un correo electrónico válido.');
      return false;
    }

    if (!validarMonto(monto)) {
      alert('Por favor, ingrese un monto válido.');
      return false;
    }

    return true;
  }

  function validarNumeroDocumento(numero) {
    return /^\d{8,}$/.test(numero);
  }

  function validarCorreo(correo) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo);
  }

  function validarMonto(monto) {
    return /^\d+(\.\d{1,2})?$/.test(monto) && parseFloat(monto) >= 0;
  }

  function enviarFormulario() {

    alert('Formulario enviado con éxito');
    formulario.reset();
  }
});
