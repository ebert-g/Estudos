from datetime import datetime
trab = {}
trab['nome'] = str(input('Nome: '))
nasci = int(input('Data de nascimento: '))
trab['idade'] = (datetime.today().year - nasci)
trab['ctps'] = int(input('CTPS[0 não possui] '))
if trab['ctps'] == 0:
    print('-=' * 30)
    for k, v in trab.items():
        print(f'    -{k} tem valor {v}')
else:
    print('-=' * 30)
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salário: R$'))
    trab['aposentadoria'] = (trab['contratação'] - nasci) + 35
    for k, v in trab.items():
        print(f'    -{k} tem valor {v}')
