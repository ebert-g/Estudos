'''matrizl1 = [[], [], []]
matrizl2 = [[], [], []]
matrizl3 = [[], [], []]
for c in range(0, 3):
    val = int(input(f'Digite um valor para [0, {c}]: '))
    matrizl1[c].append(val)
for c in range(0, 3):
    val = int(input(f'Digite um valor para [1, {c}]: '))
    matrizl2[c].append(val)
for c in range(0, 3):
    val = int(input(f'Digite um valor para [2, {c}]: '))
    matrizl3[c].append(val)

print(matrizl1)
print(matrizl2)
print(matrizl3)'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]:'))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
