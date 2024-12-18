cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para PARAR]: '))
    if n != 999:
        soma = soma + n
        cont += 1
print('Você digitous {} números e somo entre eles foi {}'.format(cont, soma))