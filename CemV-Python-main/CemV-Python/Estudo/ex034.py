s = float(input('Qual o salário do funcionario? R$: '))
if s >= 1250:
    s1 = s * 0.1
if s <= 1250:
    s1 = s * 0.15
print('o salario será: R$:{:.2f}'.format(s1 + s))
