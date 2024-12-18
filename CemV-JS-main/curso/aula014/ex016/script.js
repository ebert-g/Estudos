function contar() {
    let inicio = document.getElementById("inicio");
    let fim = document.getElementById("fim");
    let passo = document.getElementById("passo");
    let res = document.querySelector("div#res");
    let i = Number(inicio.value);
    let f = Number(fim.value);
    let p = Number(passo.value);
    res.innerHTML = ''
    if (inicio.value.length == 0) {
        res.innerHTML = 'Impossível contar!';
        return;
    }
    if (fim.value.length == 0) {
        alert('Erro! O valor de "FIM" Não foi definido.');
        return;
    }
    if (passo.value.length == 0 || p == 0) {
        alert('Erro! Valro inválido, considerando passo 1')
        p = 1;
            
    }

    if (i < f) {
        let contagem = i;
        for (i; contagem <= f; contagem += p) {
            res.innerHTML += `${contagem} \u{1F449} `;
        }
    } else {
        let contagem = i;
        for (i; contagem >= f; contagem -= p) {
            res.innerHTML += (`${contagem} \u{1F449}`);
        }
    }
    res.innerHTML += `\u{1F3C1}`;
} 