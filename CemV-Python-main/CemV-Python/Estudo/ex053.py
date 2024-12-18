#frase = (str(input('Digite um frase: ')).upper()).strip()
#fsplit = frase.split()
#fjunto = ''.join(fsplit)
#nada = ''
#for inc in range(len(fjunto), -1, -1, -1):
    #print(fjunto[inc])

frase = str('Digite uma frase: ').strip().upper()
palavras = frase. split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto)):
    print(junto[letras])