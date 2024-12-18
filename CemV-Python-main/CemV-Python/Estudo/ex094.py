pessoas = []
mulheres = []
acmedia = []
temp = {}
idade = 0
while True:
    temp['nome'] = str(input('Nome: '))
    while True:
        temp['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if temp['sexo'] in 'MF':
            break
        else:
            print('Apenas [M/F], tente novamente.')
    temp['idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    temp.clear()
    while True:
        conti = str(input('Deseja continuar?[S/N]:  ')).upper()[0]
        print('-=' * 30)
        if conti in 'SN':
            break
    if conti == 'N':
        break
for c in pessoas:
   idade += c['idade']
   if c['sexo'] == 'F':
       mulheres.append(c['nome'])
for c in pessoas:
    if c['idade'] > idade / len(pessoas):
        temp['nome'] = c['nome']
        temp['sexo'] = c['sexo']
        temp['idade'] = c['idade']
        acmedia.append(temp.copy())
        temp.clear()
print(f'Total de {len(pessoas)} pessoas cadastradas.')
print(f'A média de idade foi:  {idade / len(pessoas)}')
print(f'Mulheres cadastradas: {mulheres}')
print(f'Pessoas com idade acima da média:')
for c in acmedia:
    for k, v in c.items():
        print(f'{k} = {v}', end=' ')
    print()

