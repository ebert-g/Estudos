print('-=' * 15)
print('Vamos jogar PAR ou ÍMPAR!')
print('-=' * 15)
cont = 0
from random import randint
while True:
    n1 = int(input('Diga um valor: '))
    pi = str(input('Par ou ímpar?[P/I] : ')).upper()
    print('-' * 30)
    comp = randint(0, 10)
    if pi in 'P':
        if (n1 + comp) % 2 == 0:
            print(f'Você escolheu {n1} e o computador {comp}. A soma de {n1 + comp} = Par')
            print('Parabéns você Ganhou!')
            cont += 1
            print('-' * 30)
        elif (n1 + comp) % 2 != 0:
            print(f'Você escolheu {n1} e o computador {comp}. A soma de {n1 + comp} = Ímpar')
            print('Você Perdeu!')
            break
    elif pi in 'I':
        if (n1 + comp) % 2 != 0:
            print(f'Você escolheu {n1} e o computador {comp}. A soma de {n1 + comp} = Ímpar')
            print('Parabéns você Ganhou!')
            cont += 1
        elif (n1 + comp) % 2 == 0:
            print(f'Você escolheu {n1} e o computador {comp}. A soma de {n1 + comp} = Par')
            print('Você Perdeu!')
            break
print(f'GAME OVER! Você Ganhou {cont}', ' vezes.' if cont > 1 else 'vez')
