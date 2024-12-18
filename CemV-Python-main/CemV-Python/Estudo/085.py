valores = [list(), list()]
for c in range(0, 7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(f'Os valores pares foram {sorted(valores[0])}')
print(f'Os valores impares foram {sorted(valores[1])}')
print('Termino!')
