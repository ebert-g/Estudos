palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(c.upper(), end=': ')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print('')