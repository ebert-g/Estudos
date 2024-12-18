function GerarTab() {
    let NTab = document.querySelector("input#NTab").value;
    let ResTab = document.getElementById("ResTab");
    ResTab.value = "";
    if (NTab.length == 0) {
        alert("Erro");
        return;
    }
    for (let cont = 1; cont <= 10; cont++) {
        ResTab.value += `${NTab} x ${cont} = ${NTab * cont} \n`;
    }
}
