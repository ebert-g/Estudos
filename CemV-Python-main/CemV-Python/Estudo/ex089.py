alunos = []
tempalun = []
while True:
    tempalun.append(str(input('Nome: ')))
    tempalun.append(float(input('Nota Nº1: ')))
    tempalun.append(float(input('Nota Nº2: ')))
    alunos.append(tempalun[:])
    tempalun.clear()
    conti = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if conti in 'N':
        break
print(f'{"Nº":<5}{"ALUNO":<10}{"Média":>5}')
print('-' * 35)
for p, c in enumerate(alunos):
    print(f'{p:<5}{c[0]:<8}{(c[1] + c[2]) / 2:>5.1f}')
print('-' * 35)
while True:
    mnotas = int(input('Mostra notas de qual aluno? (999 para interrompe) : '))
    if mnotas == 999:
        break
    print(alunos[mnotas][0], alunos[mnotas][1:3])

