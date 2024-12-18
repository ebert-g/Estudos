def apjog(a='<DESCONHECIDO>', b=0):
    return f'O jogador {a} fez {b}.'


nome = str(input('Qual o nome do jogador? :'))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(apjog(b=gols))
else:
    print(apjog(nome, gols))


