por_ext = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze',
    'catorze', 'quineze', 'dezesseis', 'dezecete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '
while continuar != 'N':
    continuar = ' '
    while True:
        n = int(input('Digite um número entre 1 e 20: '))
        if 0 <= n <= 20:
            break

    print(por_ext[n])
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
 