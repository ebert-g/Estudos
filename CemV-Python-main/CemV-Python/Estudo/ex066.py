soma = 0
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'A soma dos {cont} é igual á {soma}')