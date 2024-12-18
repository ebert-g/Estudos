from ex109 import moeda
n = float((input('Digite um preço: R$')))
print(f'A metade de {moeda.fm(n)} é igual á {moeda.metade(n, f=True)} ')
print(f'O dobro de {moeda.fm(n)} é igual á {moeda.dobro(n, f=True)} ')
print(f'Aumentando {moeda.fm(n)} em 10% é {moeda.aumenta(n, 10, f=True)}')
print('FIM')
