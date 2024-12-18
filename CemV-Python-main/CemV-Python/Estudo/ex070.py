print('_' * 30)
print('     Super Mercado     ')
print('-' * 30)
menor = cont = valtot = mais_mil = 0
prod_menor = conti = ' '
while True:
    prod = str(input('Nome do Produto: '))
    val = float(input('Valor do Produto: R$:'))
    valtot += val
    cont += 1
    if val >= 1000:
        mais_mil += 1
    if cont == 1:
        prod_menor = prod
        menor = val
    else:
        if val < menor:
            prod_menor = prod
            menor = val
    conti = str(input('Deseja continuar? : ')).upper()[0]
    if conti == 'N':
        break
print('-' * 10, 'Fim do Programa', '-' * 10)
print(f'O total da compra foi de R$:{valtot:.2f}')
print(f'Temos {mais_mil} Produtos acima de R$1.000')
print(f'O Produto mais barato foi {prod_menor} com o valor de R$:{menor:.2f}')
