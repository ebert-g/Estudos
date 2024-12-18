valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    con = str(input('Deseja continuar?[S/N] : ')).upper()[0]
    if con in 'N':
        break
print(f'Você digitou {len(valores)} elementos ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if valores.count(5):
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')