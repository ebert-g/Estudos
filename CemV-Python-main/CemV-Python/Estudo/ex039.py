from datetime import datetime

nas = int(input('Qual ano de nascimento? : '))
ano = datetime.today().year
da = nas + 18
if ano - nas == 18:
    print('Aliste-se IMEDIATAMENTE!')
elif ano - nas > 18:
    print('ATRASADO em {} ano/anos'.format(ano - da))
    print('Passou do tempo se ano de alistamento foi {}'.format(da))
elif ano - nas < 18:
    print('Ainda falta {} ano/anos'.format(da - ano))
    print('Voçê ainda vai se alistar no ano {}'.format(da))