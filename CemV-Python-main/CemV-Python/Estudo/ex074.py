from random import randint

r = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(r)
print(f'O maior valor sorteado foi: {max(r)}')
print(f'O menor vlaor sorteador foi: {min(r)}')
