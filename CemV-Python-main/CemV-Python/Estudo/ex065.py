cont = n = soma = maior = menor = 0
dc = ''
while dc in 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    dc = str(input('Deseja continuar? [S/N] : ')).upper()[0]

media = soma / cont
print('Você digitou {} números e a média entre ele é {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print(f'Você digitou {cont} números e a media entre eles é {media}')
print(f'O maior valor foi {maior} e menor foi {menor}')