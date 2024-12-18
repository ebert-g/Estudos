from time import sleep
jogador = {}
gols = []
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou?: '))
for c in range(partidas):
    golsp = (int(input(f'Quantos gols na partida {c+1}: ')))
    gols.append(golsp)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
    sleep(1)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    --> Na partida {i+1}, fez {v} Gols')
    sleep(1)
print(f'Foi um total de {sum(gols)} gols')

