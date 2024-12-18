def ajuda(fun):
    info = str(input(fun))
    print('\033[1:44m~' * 30)
    print(f'Acessando o manual do comando < {info.upper()} >')
    print('~' * 30, '\033[m')
    return help(info)



while True:
    print('\033[1:42m~' * 30)
    print('   SISTEMA DE AJUDA PYTHON')
    print('~' * 30, '\033[m')
    f = ajuda('Função ou Blibioteca > ')
    if f:
        print('\033[1:41ATÉ LOGO\033[M')
        break
    print(f)