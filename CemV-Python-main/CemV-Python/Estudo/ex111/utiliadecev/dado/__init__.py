def leiadinheiro(perg):
    valid = False
    while not valid:
        n = str(input(perg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[1;31mERRO! {n} não é um preço válido.\033[m')
        else:
            valid = True
            return float(n)


