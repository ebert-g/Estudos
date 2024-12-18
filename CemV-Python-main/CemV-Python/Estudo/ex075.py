#for c in range(0, 4):
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
numeros = (n1, n2, n3, n4)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3):
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi encontrado')
print('Os números pares digitados foram: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')




'''if n1 % 2 == 0:
    print(n1, end=', ')
if n2 % 2 == 0:
    print(n2, end=', ')
if n3 % 2 == 0:
    print(n3, end=', ')
if n4 % 2 == 0:
    print(n4)'''