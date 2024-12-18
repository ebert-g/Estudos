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
