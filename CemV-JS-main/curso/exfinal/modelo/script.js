let ListaNum = [];
let DivRes = document.querySelector("#res");
let SelRes = document.querySelector("#SelRes");
let ninp = document.querySelector("#InpNum");
function add() {
    let entNum = document.querySelector("#InpNum").value;
    DivRes.innerHTML = "";
    if (entNum.length == 0 || Number(entNum) > 100 || Number(entNum) < 1) {
        alert(`Erro! Valor incorreto. Tente Novamente`);
    } else if (ListaNum.includes(Number(entNum))) {
        alert("Erro! Valor já incluido.");
    } else {
        let InpNum = Number(entNum);
        ListaNum.push(InpNum);
        let item = document.createElement("option");
        item.text = `Valor ${InpNum} adicionado.`;
        SelRes.appendChild(item);
        console.log(ListaNum);
    }
    ninp.value = "";
    ninp.focus();
}

function AnalisandoLista() {
    if (ListaNum.length == 0) {
        alert("Erro colocque um valor antes de finalizar");
    } else {
        let c = 0;
        let maior, menor;
        let total = 0;
        while (c < ListaNum.length) {
            total += ListaNum[c];
            if (c == 0) {
                maior = ListaNum[c];
                menor = ListaNum[c];
            } else {
                if (ListaNum[c] > maior) {
                    maior = ListaNum[c];
                }
                if (ListaNum[c] < menor) {
                    menor = ListaNum[c];
                }
            }
            c += 1;
        }

        let media = (total / ListaNum.length) | 0;

        DivRes.innerHTML = `Ao todo, temos ${ListaNum.length} números cadastrados.<br>`;
        DivRes.innerHTML += `O menor valor informado foi ${menor}<br>`;
        DivRes.innerHTML += `O maior valor informado foi ${maior}<br>`;
        DivRes.innerHTML += `Somando todos os valores, temos ${total}<br>`;
        DivRes.innerHTML += `A média dos valores digitados é : ${media}`;
    }
}
