# criação da matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
print('-=' * 30)
# MOSTRANDO MATRIZ
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 30)
soma = maior = soma3c = 0
for c in range(0, 3):
    if matriz[c][2]:
        soma3c += matriz[c][2]
    for l in range(0, 3):
        if matriz[c][l] % 2 == 0:
            soma += matriz[c][l]
        if c == 0 and l == 0:
            maior = matriz[1][l]
        else:
            if matriz[1][l] > maior:
                maior = matriz[1][l]
# 'PRINTS'
print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da 3ª coluna é: {soma3c}')
print(f'O maior valor da segunda coluna é : {maior}')
