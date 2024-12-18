from random import randint

'''contN = 1
randnum = randint(0, 10)
n = int(input('Acabei de pensar em um número entre 0 e 10\nSerá que voçê consegue adivinhar? Diga um número : '))
while n != randnum:
    contN += 1
    if n < randnum:
        n = int(input('Mais... Tente novamente : '))
    elif n > randnum:
        n = int(input('Menos tente novamente : '))
print('A maquina pensou em {}'.format(randnum))
print('Parabéns você acertou em {} tentativas'.format(contN))'''


nran = randint(0, 10)
n = False
contn = 0
print('olá sou seu computador! Pesnsei em um número será que você consegue adivinhar?')
while not n:
    contn += 1
    jogador = int(input('Digite um número: '))
    if jogador == nran:
        n = True
    if jogador > nran:
        print('Menos... Tente novamente! ')
    elif jogador < nran:
        print('Mais... Tente novamente!')

print('Parebéns você acertou! O computador pensou em {} '.format(nran))
print('Você levou {} tentativas'.format(contn))