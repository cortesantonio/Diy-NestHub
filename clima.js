// URL de la solicitud a la API de OpenWeatherMap
var url = "https://api.openweathermap.org/data/2.5/weather?q=Curico&appid=aff2a052f9fe5374c9aba06c1039b674";
// Realizar la solicitud utilizando Fetch API
fetch(url)
    .then(response => response.json())
    .then(data => {
        // Extraer los datos del clima de la respuesta JSON
        var temperaturaKelvin = data.main.temp;
        var temperaturaCelsius = temperaturaKelvin - 273.15; // Conversión a Celsius
        var iconoClima = data.weather[0].icon;

        // Hacer algo con los datos obtenidos, como mostrarlos en la página
        document.getElementById("temperatura").textContent = temperaturaCelsius.toFixed(1) + " °C"; // Mostrar temperatura con 2 decimales
        document.getElementById("icono-clima").src = "http://openweathermap.org/img/w/" + iconoClima + ".png";
    })
    .catch(error => {
        console.log("Error al obtener datos del clima:", error);
    });