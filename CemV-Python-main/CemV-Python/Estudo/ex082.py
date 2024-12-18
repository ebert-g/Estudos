valores = []
valpar = []
valimp = []
while True:
    valores.append(int(input('Digite um valor: ')))
    conti = str(input('Deseja continuar?[S/N] : ')).upper()[0]
    if conti in 'N':
        break
print(f'Lista completa: {valores}')
for par in valores:
    if par % 2 == 0:
        valpar.append(par)
    else:
        valimp.append(par)
print(f'Valores pares da lista: {valpar}')
print(f'Valores impares da lista: {valimp}')
