soma = 0
quant = 0
for c in range(1, 7):
    c = int(input('Digite o {}º número: '.format(c)))
    if c % 2 == 0:
        soma = soma + c
        quant = quant + 1
print('{} números eram pares e a soma dos mesmos é igual é igual á: {}'.format(quant, soma))