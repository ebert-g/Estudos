lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Valor Adicionado.')
    elif n > lista[-1]:
        lista.append(n)
        print('Valor Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor Adicionado na posição {pos}')
                break
            pos += 1
print(lista)
