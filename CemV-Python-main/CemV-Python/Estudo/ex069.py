tot18 = h = m20 = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA     ')
    print('-' * 30)
    idade = int(input('Qual a sua idade: '))
    if idade >= 18:
        tot18 += 1
    sex = str(input('Qual o seu sexo [M/F]: ')).upper()[0]
    if sex == 'M':
        h += 1
    if sex == 'M' and idade < 20:
        m20 += 1
    print('- ' * 15)
    pros = str(input('Quer continuar?[S/N] : ')).upper()[0]
    if pros == 'N':
        break
print(f'Total de pessoas com +18: {tot18}')
print(f'Total de Homens cadastrados: {h}')
print(f'Total de Mulheres com mais de 20 anos: {m20}')
