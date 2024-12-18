print('Gerador de PA!')
primeiro = int(input('Qual o primeiro termo? : '))
raz = int(input('Qual a Razão? : '))
cont = 1
termo = primeiro
maistermos = 1
while cont <= 10:
    cont += 1
    print(termo, end='')
    print(' -> ' if cont < 11 else ' : PAUSA', end='')
    termo += raz
while maistermos != 0:
    maistermos = int(input('\nQuantos termos você quer mostrar a mais? : '))
    if maistermos != 0:
        for c in range(maistermos):
            cont += 1
            print(termo, end=' -> ')
            termo += raz