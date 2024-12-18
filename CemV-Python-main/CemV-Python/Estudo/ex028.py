from random import randint
from time import sleep
""" n1 = int(input('acerte o número de 1 á 5 que o computador vai sortear: '))
n = randint(1, 5)
print('Número sorteado: {}'.format(n))
if n1 == n:
    print('PARABÉNS!! Voçê ACERTOU!'.upper())
else:
    print('ERRRRROOOU!!') """

# OPÇÃO 2
print('-=-' * 25)
print('Vou pensar em número de 0 á 5. Tente advinhar: ')
print('-=-' * 25)
n = randint(0, 5)
n1 = int(input('Em qual número eu pensei? : '))
print('PROCESSANDO...')
sleep(3)
if n1 == n:
    print('Parabéns, Voçê ganhou!!')
else:
    print('GANHEI!! E VC SE FUDEU ERA O NÚMERO {}'.format(n))

