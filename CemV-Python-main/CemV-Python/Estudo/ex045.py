from random import randint
lista = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('#' * 25)
print('Pedra, Papel ou Tesoura')
print('#' * 25)
jog = int(input('''Vamos Jogar, Escolha uma das opções: 
[0] - Pedra
[1] - Papel
[2] - Tesoura
R:'''))
if pc == 0: # PC PEDRA
    if jog == 0:
        print('Empate! você escolher pedra e o computador também')
    elif jog == 1:
        print('Ganhou! você escolheu Papel e o computador Pedra ')
    elif jog == 2:
        print('Perdeu! Você escolher Tesoura e computador Pedra')
elif pc == 1: # PC PAPEL
    if jog == 0:
        print('Perdeu! Você escolheu Pedra e o computador Papel ')
    elif jog == 1:
        print('Empate! Você escolheu Papel e o computador também ')
    elif jog == 2:
        print('Ganhou! Você escolheu Tesoura e o computador Papel ')
elif jog == 2: #PC TESOURA
    if jog == 0:
        print('Ganhou! Você escolheu Pedra e o computador Tesoura')
    elif jog == 1:
        print('Perdeu! Você escolheu Papel e o computador Tesoura')
    elif jog == 2:
        print('Empate! Você escolher Tesoura e o computador também')
else:
    print('Jogada inválida')