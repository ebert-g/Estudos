def leiaint(perg):
    while True:
        val = str(input(perg)).strip()
        if val.isnumeric():
            return val
            break
        else:
            print('\033[1:31mERRO! ENTRADA INVÁLIDA, DIGITE UM NÚMERO\033[m')


n = leiaint('Digite um número: ')
print(f'\033[1:32mVocê acabou de digitar o número  [ {n} ]\033[m')
