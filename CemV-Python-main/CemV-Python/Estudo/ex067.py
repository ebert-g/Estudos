cont = 0
while True:
    print('-' * 40)
    tab = int(input('Quer ver a tabuada de qual número? : '))
    print('-' * 40)
    if tab <= 0:
        break
    elif tab > 0:
        for c in range(1, 11):
            mult = tab * c
            print(f'{tab} x {c} = {mult}')
print('Obrigado por participar!')
