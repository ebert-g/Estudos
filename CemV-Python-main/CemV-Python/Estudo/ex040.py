n1 = float(input('Qual a primeira nota? : '))
n2 = float(input('Qual a segunda nota? : '))
media = (n1 + n2) / 2
print('Sua média foi {}'.format(media))
if media < 5:
    print('Você foi REPROVADO!')
elif 5 <= media < 7 :
    print('voçê está de RECUPERAÇÃO!')
elif media >= 7:
    print('Voçê está APROVADO!')
