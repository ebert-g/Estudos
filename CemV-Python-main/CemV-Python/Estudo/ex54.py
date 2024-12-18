from datetime import date
cont18 = 0
cont00 = 0
contp = 0
for c in range(1, 8):
    contp = contp + 1
    idade = int(input('Em qual ano o {}º nasceu?: '.format(contp)))
    if date.today().year - idade >= 18:
        cont18 = cont18 + 1
    else:
        cont00 = cont00 + 1
print('Ao todos {} eram maiores de idade e \n {} eram menores de idade'.format(cont18, cont00))