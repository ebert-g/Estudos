termo = int(input('Quantos termos você quer mostrar? : '))
cont = 0
termo_1 = 0
termo_2 = 1
print('0 -> 1 ->', end='')
while cont < (termo - 2):
    termo_r = termo_1 + termo_2
    print(' {} -> '.format(termo_r), end='')
    termo_1 = termo_2
    termo_2 = termo_r
    cont += 1
print('FIM')
