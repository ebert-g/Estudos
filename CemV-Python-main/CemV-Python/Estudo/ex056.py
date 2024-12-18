pes = 0
midade = 0
maisv = 0
nomev = ''
mu20 = 0
for c in range(1, 5):
    pes += 1
    print('---- info da {}ª pessoa ----'.format(pes))
    nome = str(input('Qual o seu nome?: ')).upper()
    idade = int(input('Qual a sua idade? : '))
    sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()
    midade = (midade + idade)
    if sexo == 'F':
        if idade < 20:
            mu20 += 1

    if sexo == 'M':
        if idade == 1:
            maisv = c
        else:
            if idade > maisv:
                maisv = idade
                nomev = nome

print('À média de idade corresponde á: {}'.format(midade / 4))
print('o homem mais velho se chama {} e tem {} anos'.format(nomev, maisv))
print('Ao todos são {} mulheres menores que 20 anos'.format(mu20))
