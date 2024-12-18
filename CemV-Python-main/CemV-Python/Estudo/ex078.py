valores = list()
pmaior = []
pmenor = []
for c in range(0, 5):
    valores.append(int(input('Digite um Valor: ')))
print(f'Os valores digitados foram {valores}')
maior = menor = cont = 0
for pos, c in enumerate(valores):
    cont += 1
    if cont == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c

for pos1, c1 in enumerate(valores):
    if c1 == maior:
        pmaior.append(pos1)
    if c1 == menor:
        pmenor.append(pos1)

print(f'O maior número digitado foi {maior} nas posições {pmaior}')
print(f'O menor número digitado  foi {menor} nas posições {pmenor} ')

