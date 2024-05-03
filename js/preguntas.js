function toggleFaq(index) {
    const answer = document.querySelectorAll('.answer')[index - 1];
    const arrow = document.querySelectorAll('.arrow')[index - 1];
    const isOpen = answer.style.display === 'block' || answer.style.display === '';

    // Oculta todas las respuestas y resetea las flechas
    document.querySelectorAll('.answer').forEach(a => a.style.display = 'none');
    document.querySelectorAll('.arrow').forEach(a => a.style.transform = 'rotate(0deg)');

    // Muestra la respuesta si no está abierta, o la oculta si ya está abierta
    answer.style.display = isOpen ? 'none' : 'block';

    // Rota la flecha solo si no se está moviendo
    if (!isOpen) {
        arrow.style.transform = 'rotate(180deg)';
    }
}
