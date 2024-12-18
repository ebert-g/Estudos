from random import randint
from time import sleep
from operator import itemgetter
rank = []
jogadores = {'1': randint(1, 6), '2': randint(1, 6),
             '3': randint(1, 6), '4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar: Jogador {v[0]} com {v[1]}')
    sleep(1)