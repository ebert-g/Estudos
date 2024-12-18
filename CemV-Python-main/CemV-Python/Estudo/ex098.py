from time import sleep


def cont(com, fi, pas):
    print(f'Contagem de {com} até {fi} de {pas} em {pas}:')
    if pas * -1 > 0:
        pas = pas * -1
    if com > fi:
        fi = fi - pas
        pas = -pas
    if fi > com:
        fi = fi + 1
    if pas == 0:
        pas = 1
    for c in range(com, fi, pas):
        print(f'{c} ', end='')
        sleep(0.3)
    print(' ->FIM')
    print('-' * 60)


cont(1, 10, 1)
cont(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
print('-' * 60)
cont(i, f, p)
