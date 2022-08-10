const url = 'https://api.crhoy.net/ultimas/5.json';
const root = document.getElementById('root')
fetch(url)
    .then(res => res.json())
    .then(response => {
        lista= response.ultimas

        for (let index = 0; index < lista.length; index++) {
            const N = lista[index]
            const card = document.createElement("div");
            card.classList.add("tarjeta")

            //titulo
            const tituloNota = document.createElement("p")
            tituloNota.innerHTML = N.title;
            tituloNota.classList.add("titulo-notas")
            
            //imagen 
            const descripcionNota = document.createElement("img")
            descripcionNota.src = N.img;
            descripcionNota.classList.add("img-notas")
            //hora 
            const hora = document.createElement('div')
            hora.innerHTML = N.hour
            hora.classList.add('hora')
            // enlace
            const url = document.createElement('a')
            url.href=N.url;
            url.innerHTML = '<i class="fa-solid fa-angle-right"></i>'
            url.classList.add('enlace')



            card.appendChild(descripcionNota);
            card.appendChild(tituloNota)
            card.appendChild(hora)
            card.appendChild(url)
            root.appendChild(card)
        }

    })
