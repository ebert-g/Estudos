function Dahora(){
    let text = document.getElementById('TxtSection')
    let img = window.document.getElementById("img")
    let HoraAtual = new Date()
    let hora = HoraAtual.getHours()
    text.innerHTML = `Agora são ${hora} horas`
    if(hora >= 0 && hora < 12){
        //Dia
        img.src = 'ftdia-250.png'
        document.body.style.background = '#a5bdd1'
    }
    else if(hora >= 12 && hora < 18){
        //tarde
        img.src = 'fttarde-250.png'
        document.body.style.background = '#a76b66'

    }
    else{
        //noite
        img.src = 'ftnoite-250.png'
        document.body.style.background = '#7f5968'
    }

}