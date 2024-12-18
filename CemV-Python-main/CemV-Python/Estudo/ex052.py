n = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
        print('\033[36m', c,'\033[m', end=' ')
    else:
       print('\033[31m', c, '\033[m',  end=' ')
if cont == 2:
    print('\n Número primo')
else:
    print('\n Não é número primo')
