from random import randint
from time import sleep
jogos = []
tempjogo = []
print('=' * 30)
print(f'{'CRIAR JOGOS MEGA SENA':^30}')
print('=' * 30)
njogos = int(input('Quantos jogos da MEGA SENA você precisa? : '))
for c in range(njogos):
    while True:
        nal = randint(1, 60)
        if nal not in tempjogo:
            tempjogo.append(nal)
        if len(tempjogo) == 6:
            break
    jogos.append(sorted(tempjogo[:]))
    tempjogo.clear()
print('-=' * 8, f'SORTENADO {njogos} JOGOS', '-=' * 8)
for c in range(njogos):
    sleep(1)
    print(f'Jogo Nº{c+1}', end=': ')
    for l in range(len(jogos[c])):
        print(f'[{jogos[c][l]:^4}]', end=' ')
    print()

