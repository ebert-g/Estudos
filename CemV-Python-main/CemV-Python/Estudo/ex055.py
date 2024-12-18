maiorp = 0
menorp = 0
for pess in range(1, 6):
    peso = float(input('Qual peso da {}ª pessoa (Kg): '.format(pess),))
    if pess == 1:
        maiorp = pess
    else:
        if peso > maiorp:
            maiorp = peso
    if pess == 1:
        menorp = pess
    else:
        if menorp < peso:
            menor = peso

print('O maior peso lido foi: {} \nO menor peso lido foi: {} '.format(maiorp, menorp))
