const url = 'https://api.crhoy.net/ultimas/5.json';
const root = document.getElementById('root')
fetch(url)
    .then(res => res.json())
    .then(response => {
        lista = response.ultimas
        for (let index = 0; index < 4; index++) {
            const N = lista[index]
            const url = document.createElement('a')
            url.href = N.url;
            url.classList.add('enlace')
            const card = document.createElement("div");
            card.classList.add("tarjeta")
            const tituloNota = document.createElement("p")
            tituloNota.innerHTML = N.title;
            tituloNota.classList.add("titulo-notas")
            const descripcionNota = document.createElement("img")
            descripcionNota.src = N.img;
            descripcionNota.classList.add("img-notas")
            const hora = document.createElement('div')
            hora.innerHTML = N.hour
            hora.classList.add('hora')
            url.appendChild(descripcionNota);
            url.appendChild(hora)
            url.appendChild(tituloNota)
            card.appendChild(url)
            root.appendChild(card)
        }

    })
