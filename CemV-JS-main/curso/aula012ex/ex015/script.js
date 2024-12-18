function verificar() {
    let Data = new Date();
    let AnoAtual = Data.getFullYear();
    let AnoNasc = document.getElementById("AnoNasc");
    let res = document.querySelector("div#res");
    if (AnoNasc.value.length == 0 || AnoNasc.value > AnoAtual) {
        alert("Erro! Entrada incorrta Tente novamente.");
    } else {
        let sex = document.getElementsByName("radsex");
        let idade = AnoAtual - Number(AnoNasc.value);
        let SexSelect = "";
        let img = document.createElement("img");
        img.setAttribute("id", "foto");
        if (sex[0].checked) {
            SexSelect = "Homem";
            if (idade >= 0 && idade < 15) {
                //menino
                img.setAttribute("src", "menino.png");
            } else if (idade > 15 && idade < 50) {
                //homem
                img.setAttribute("src", "homem.png");
            } else {
                //idoso
                img.setAttribute("src", "idoso.png");
            }
        } else if (sex[1].checked) {
            SexSelect = "Mulher";
            if (idade > 0 && idade < 15) {
                //menina
                img.setAttribute("src", "menina.png");
            } else if (idade > 15 && idade < 50) {
                //mulher
                img.setAttribute("src", "mulher.png");
            } else {
                //idosa
                img.setAttribute("src", "idosa.png");
            }
        }
        res.style.textAlign = "center";
        res.innerHTML = `Detectamos ${SexSelect} com ${idade} Anos`;
        res.appendChild(img);
    }
    function tetst() {
        let eka = "Tes";
    }
}
