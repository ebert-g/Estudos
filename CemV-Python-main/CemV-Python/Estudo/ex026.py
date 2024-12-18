
frase = str(input('Digite uma frase: ')).lower().strip()
print('\033[1;31mExiste {} "a" na sua frase\033[m'.format(frase.count('a')))
print('o primeiro "a" está na posição {}'.format(frase.find('a') + 1))
print('o último "a" aparece na posição {}'.format(frase.rfind('a') + 1))
