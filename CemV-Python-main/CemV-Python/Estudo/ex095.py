jogadores = []
temp = {}
gols = []
while True:
    temp['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantos partidas {temp["nome"]} jogou : '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols {temp["nome"]} na {c+1}º partida: ')))

    temp['gols'] = gols[:]
    temp['total'] = sum(gols)
    gols.clear()
    jogadores.append(temp.copy())
    temp.clear()
    while True:
        conti = str(input('Deseja continuar?[S/N]: ')).upper()[0]
        if conti in 'SN':
            break
    print('-*-' * 20)
    if conti == 'N':
        break
print('-' * 60)
print(f'{"Cod"}     {"nome"}        {"Gols":}               {"Total"}')
for i, c in enumerate(jogadores):
    print(f'{i}     {c["nome"]}     {c["gols"]}             {c["total"]}')
print('-' * 60)
while True:
    while True:
        levante = int(input('Mostras dados de qual jogador?[999 para parar] : '))
        if levante == 999:
            break
        if levante > len(jogadores):
            print('Escolha incorreta! Tente Novamente ou 999 para encerrar.')
        else:
            break
    if levante == 999:
            break
    print(f' - - - Levantamento do Jogador {jogadores[levante]["nome"]} - - - ')
    for i, c in enumerate(jogadores[levante]['gols']):
        print(f'    No jogo {i+1} fez {c}')
print('<<< Encerrando >>>')

