from ex107 import moeda
n = float((input('Digite um preço: R$')))
print(f'A metade de {n} é igual á {moeda.metade(n)} ')
print(f'O dobro de {n} é igual á {moeda.dobro(n)} ')
print(f'Aumentando {n} em 10% é {moeda.aumenta(n, 10)}')
print('FIM')