print('->' * 20)
vel = int(input('Qual a velocidade do carro?:'))
print('<-' * 20)
if vel <= 80:
    print('Tudo bem Dirija com segurançã')
else:
    print('!!!MULTADO!!! Voçe será multado em R$: {:.2f}'.format((vel - 80) * 7))
