def fatorial(f, show=False):
    tot = 1
    for c in range(f, 0, -1):
        tot *= c
        if show:
            print(f'{c}', end=' x ')
    return tot


print(fatorial(6, True))
