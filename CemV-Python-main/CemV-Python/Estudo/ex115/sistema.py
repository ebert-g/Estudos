from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cadastro.txt'
if abri_arq(arq):
    criar_arq(arq)
while True:
    titulo('MENU PRINCIPAL')
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do Progrema!'])
    if resp == 1:
        titulo('VER PESSOAS CADASTRADAS')
        ler_arq(arq)
    elif resp == 2:
        titulo('NOVO CADASTRO')
        cadastrar()
    elif resp == 3:
        titulo('SAINDO DOS SISTEMA!')
        break
    else:
        print(cores(1), 'Erro! Digite uma opçao válida.', cores())
    sleep(2)
