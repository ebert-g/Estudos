val_user = []
contin = ' '
while True:
    val = int(input('Digite um valor: '))
    if val not in val_user:
        val_user.append(val)
        print(f'Valor {val} adicionado com sucesso!')
        print('=' * 30)
    else:
        print('Valor duplicado. Descartado!')
    contin = str(input('Deseja continuar?[S/N] : ')).upper()[0]
    if contin == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(val_user)}')

