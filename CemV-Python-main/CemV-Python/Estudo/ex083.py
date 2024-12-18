exp = str(input('Digite uma Expressão númerica: '))
'''abri = exp.count('(')
fecha = exp.count(')')
print(abri)
print(fecha)
if abri == fecha:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!'''
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão esta incorreta!')
