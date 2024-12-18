v1 = float(input('Qual o primeiro vertice? : '))
v2 = float(input('Qual o segundo vertice? : '))
v3 = float(input('Qual o terceiro vertice? : '))
# POSSIBILADE DE TRIANGULO
if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    if v1 == v2 == v3:
        print('Triângulo EQUILÁTERO')
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print('Triângulo ISÓCELES')
    elif v1 != v2 != v3 != v1:
        print('Triângulo ESCALENO')
else:
    print('Não é possivél fazer um triângulo')
