print('=' * 40)
print('{:^40}'.format('BANCO'))
print('=' * 40)
val = int(input('Qual Valor você quer sacar? : R$:'))
n50 = n20 = n10 = n1 = 0
while True:
    if val % 50 > 0:
        n50 = val // 50
        sobra = val % 50
    else:
        n50 = val // 50
        break
    if sobra > 0:
        n20 = sobra // 20
        sobra = sobra % 20
    else:
        n20 = sobra // 20
        break
    if sobra > 0:
        n10 = sobra // 10
        sobra = sobra % 10
    else:
        n10 = sobra // 10
        break
    if sobra > 0:
        n1 = sobra // 1
        break
#print(f'''Total de notas de R$: 50,00 : {n50}
#Total de notas de R$: 20,00 : {n20}
#Total de notas de R$: 10,00 : {n10}
#Total de notas de R$: 1,00 : {n1}''')
if n50 > 0:
    print(f'Total de notas de R$:50,00: {n50}')
if n20 > 0:
    print(f'Total de notas de R$:20,00 : {n20}')
if n10 > 0:
    print(f'Total de notas de R$:10,00 : {n10}')
if n1 > 0:
    print(f'Total de notas de R$:1,00 : {n1}')