def metade(v,):
    met = v / 2
    return met


def dobro(v):
    dob = v * 2
    return dob

def aumenta(v, p):
    porc = v * (p / 100)
    aum = v + porc
    return aum
def diminuir(v):
    porc = v * (p / 100)
    aum = v - porc
    return aum

def fm(v):
    return f'R${v:>.2f}'.replace('.', ',')