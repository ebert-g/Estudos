aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situ'] = 'Aprovado'
elif 5 < aluno['média'] < 7:
    aluno['situ'] = 'Recuperação'
else:
    aluno['situ'] = 'Reprovado'
print(f'Nome é igual á {aluno["nome"]}')
print(f'A Média é igual á {aluno["média"]} ')
print(f'A situação é igual á {aluno["situ"]}')
print(aluno)
