print('=>' * 25)
print('DIGITE A MÉDIDA DO TRIÂNGULO')
print('=>' * 25)
m1 = int(input('Digite o valor da 1° Reta: '))
m2 = int(input('Digite o valor da 1° Reta: '))
m3 = int(input('Digite o valor da 1° Reta: '))
if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    print('=' * 30)
    print('As restas {}, {},  {} podem forma um triângulo!'.format(m1, m2, m3))
    print('=' * 30)
else:
    print('Não é possível forma um triângulo')
