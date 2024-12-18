def fm(v):
    return f'R${v:>.2f}'.replace('.', ',')


def metade(v, f=False):
    met = v / 2
    if f:
        return fm(met)
    else:
        return met


def dobro(v, f=False):
    dob = v * 2
    if f:
        return fm(dob)
    else:
        return dob


def aumenta(v, p, f=False):
    porc = v * (p / 100)
    aum = v + porc
    if f:
        return fm(aum)
    else:
        return aum


def diminuir(v, p, f=False):
    porc = v * (p / 100)
    dim = v - porc
    if f:
        return fm(dim)
    else:
        return dim


def resumo(v=0, au=0, di=0):
    res_metade = metade(v,True)
    res_dobro = dobro(v,True)
    res_aument = aumenta(v, au, True)
    res_dim = diminuir(v, di, True)
    titulo('Resumo do valor')
    print(f'Analisando o Valor: {fm(v)}')
    print(f'Dobro: \t\t\t\t{res_dobro}')
    print(f'Metade: \t\t\t{res_metade}')
    print(f'{au}% de Aumento: \t{res_aument}')
    print(f'{di}% de Redução: \t{res_dim}')


def titulo(txt):
    print('-' * (len(txt) + 14))
    print(f'       {txt}')
    print('-' * (len(txt) + 14))
