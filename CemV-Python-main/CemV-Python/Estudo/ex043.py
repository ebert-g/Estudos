alt = float(input('Qual a sua altura?(m): '))
pes = float(input('Qual o seu peso?(kg) : '))
imc = pes / (alt * alt)
if imc < 18.5:
    print('IMC: {:.1f}, Abaixo do peso'.format(imc))
elif 18.5 < imc < 25:
    print('IMC: {:.1f}, Peso ideal'.format(imc))
elif 25 < imc < 30:
    print('IMC: {:.1f}, Sobrepeso'.format(imc))
elif 30 < imc < 40:
    print('IMC: {:.1f}, Obesidade'.format(imc))
else:
    print('IMC: {:.1f}, Obesidade mórbida'.format(imc))
