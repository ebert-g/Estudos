soma = 0
quant = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        quant = quant + 1
        soma = soma + c
print('Existe {} itens e a soma de todos eles é igual {}'.format(quant, soma))