from time import sleep
n1 = int(input('Qual o primeiro valor: '))
n2 = int(input('Qual o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''     [1] - Somar
     [2] - Multiplicar
     [3] - Maior
     [4] - Novos números
     [5] - Sair do Programa''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))

    elif opcao == 2:
        produto = n1 * n2
        print('{} x {} = {}'.format(n1, n2, produto))

    elif opcao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2

    elif opcao == 4:
        n1 = int(input('Qual o primeiro valor: '))
        n2 = int(input('Qual o segundo valor: '))

    elif opcao == 5:
        print('Volte sempre')
    else:
        print('Inválido. Tente novamente.')
    print('-=-' * 20)
    sleep(2)