sex = str(input('informe o seu sexo? (M/F) : ')).upper().strip()[0]
while sex not in 'FM':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: (M/F) : ')).strip().upper()[0]
if sex == 'M':
        sex = 'Masculino'
elif sex == 'F':
        sex = 'Feminino'
print('{} registrado com sucesso. Obrigado!'.format(sex))
