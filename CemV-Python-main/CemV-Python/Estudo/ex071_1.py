print('=' * 40)
print('{:^40}'.format('BANCO'))
print('=' * 40)
val = int(input('Qual Valor você quer sacar? : R$:'))
total = val
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced >= 1:
            print(f'Total de {totced} de R$: {ced},00 ')
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
