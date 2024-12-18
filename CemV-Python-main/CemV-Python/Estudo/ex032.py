from datetime import date
ano = int(input('Vamos analisar um ano. Diite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:
    print('o ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} Não é bissexto'.format(ano))