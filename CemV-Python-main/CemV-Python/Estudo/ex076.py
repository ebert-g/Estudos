tabela = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo',
          25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
          120.00, 'Canetas', 22.30, 'Livro', 34.90)
print('_' * 40)
print('{:^40}'.format('Lista de Preços'))
print('_' * 40)
for c in range(0, len(tabela), 2):
    #print('{:^} {:.^15} R$: {:.2f}'.format(tabela[c], '', tabela[c + 1]))
    print(f'º{tabela[c]:.<40} R${tabela[c + 1]:^5.2f}')
print('_' * 40)
