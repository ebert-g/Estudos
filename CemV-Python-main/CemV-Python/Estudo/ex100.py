from time import sleep
from random import randint
val = []


def sorteio(n):
    val.clear()
    for c in range(n):
        val.append(randint(1, 10))
    print(f'Sorteando os valores da lista: ', end='')
    for c in val:
        print(f'{c} ', end='')
        sleep(0.5)
    print('Pronto')


def somap():
    somar = 0
    for c in val:
        if c % 2 == 0:
            somar += c
    print(f'Somandos os valores pares de {val}, temos {somar}')


sorteio(4)
somap()
sorteio(3)
somap()
sorteio(10)
somap()
