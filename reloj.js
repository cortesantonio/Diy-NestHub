function mostrarHoraActual() {
    var fecha = new Date();
    var horas = fecha.getHours();
    var minutos = fecha.getMinutes();
    var segundos = fecha.getSeconds();

    var horaActual = horas + ":" + minutos;

    document.getElementById("hora").textContent = horaActual;
}

// Actualizar la hora cada segundo
setInterval(mostrarHoraActual, 1000);