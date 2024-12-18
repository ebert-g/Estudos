let num = [0, 3, 5, 7, 4, 2];
num.push(3);
num.sort();
//console.log(num)
/*for (let c = 0; c < num.length; c++) {
    console.log(`A posição ${c} tem o valor ${num[c]}`);
}
console.log("-----------------------------");
cont = 0;
while (cont < num.length) {
    console.log(`Na posição ${cont} está ${num[cont]}`)
    cont++
}
console.log("-----------------------------")
contador = 0
do{
    console.log(`Na posição ${contador} está ${num[contador]}`)
    contador++

}while(contador<num.length)*/
let pos = 0;
for (let pos in num) {
    console.log(`Na parada ${pos} o elemento é ${num[pos]}`);
}
