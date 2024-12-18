pess_temp = []
pessoas = []
mai = men = 0
while True:
    pess_temp.append(str(input('Nome: ')))
    pess_temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = pess_temp[1]
    else:
        if pess_temp[1] > mai:
            mai = pess_temp[1]
        if pess_temp[1] < men:
            men = pess_temp[1]
    pessoas.append(pess_temp[:])
    pess_temp.clear()
    qconti = str(input('Deseja continuar? [s/n]: ')).upper()[0]
    if qconti in 'N':
        break

print('-=' * 30)
print(f'Total de pessoas cadastradas : {len(pessoas)}')
print(f'O maior peso foi {mai}Kg.', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
        print()
print(f'O menor peso foi {men}Kg.', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
