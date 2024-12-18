val = float(input('Qual o valor do produto? :R$ '))
#FORMA DE PAGAMENTO:
c = int(input('Qual será a forma de pagamento?'
      ' \n [1] - À vista '
      '\n [2] - A vista no cartão '
      '\n [3] - Até 2x no cartão '
      '\n [4] - 3x ou mais no cartão'
              '\n Escolha uma forma de pagamento: '))
if c == 1:
    print('Com 10% de desconto o valor será: R$ {}'.format(val - (val * 0.1)))
elif c == 2:
    print('Com 5% de desconto o valor será: R$ {}'.format(val - (val * 0.05)))
elif c == 3:
    print('O valor será R$ {}'.format(val))
elif c == 4:
    par = int(input('Em quantas vezes vai dividir? : '))
    valpar = (val + (val * 0.2)) / par
    print('O valor será R$ {} com {} parcelas de {}'.format(val + (val * 0.2), par, valpar))
