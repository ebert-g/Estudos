def leiaint(perg):
    while True:
        try:
            val = int(input(perg))
        except (ValueError, TypeError):
            print('\033[1;31mEntrada Inválida. Por favor digite um número inteiro\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;33mParece que o úsuario não quis continuar\033[m')
            return 0
            break
        else:
            return val


def leiafloat(perg):
    while True:
        try:
            val = float(input(perg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[1;31mEntrada inválida. Digite um número Real.\033[m')
        except KeyboardInterrupt:
            print('Parece que o úsuario não quis continuar')
            return 0
            break
        else:
            return val


n = leiaint('Digite um número inteiro: ')
print(f'O valor digitado foi {n}')
nfloat = leiafloat('Digite um número Real: ')
print(f'O valor digitado foi {nfloat}')
