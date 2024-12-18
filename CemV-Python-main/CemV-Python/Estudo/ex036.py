casa = float(input('Qual o valor da CASA? : R$ '))
sal = float(input('Qual o seu Salário? : R$ '))
anos = int(input('Em quantos anos voçê vai pagar? : '))
par = casa / (anos * 12)
if par <= 0.3 * sal:
    print('O financiamento pode ser realizado as parcelas serão de R$ {:.2f}'.format(par))
else:
    print('As parcelas de R$ {:.2f} excedem 30% do valor do seu salário, o financiamento NÃO pode ser realizado'.format(par))
