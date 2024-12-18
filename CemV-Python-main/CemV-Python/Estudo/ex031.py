dist = float(input('\033[1;38;mQual a distância da sual viagem? \033[m'))
if dist <= 200:
    print('O valor da sua viagem será: {:.2f} '.format(dist * 0.50))
else:
    print('O valor da sua viagem será: {:.2f}'.format(dist * 0.45))
