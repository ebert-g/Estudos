from datetime import datetime

nas = int(input('Qual ano voçê nasceu? : '))
ano = datetime.today().year
idade = ano - nas
if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('CategoriA: INFANTIL')
elif 14 < idade <= 19:
    print('Categoria: JUNIOR')
elif 19 < idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: Master')
