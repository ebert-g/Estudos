from time import sleep


def maior(*num):
    mai = 0
    for i, c in enumerate(num):
        if i == 0:
            mai = c
        else:
            if c > mai:
                mai = c
    print(f'Analisando os números...')
    for c in num:
        print(f'{c}, ', end='')
        sleep(1)
    print(f'Foram informados {len(num)} números')
    if len(num) > 0:
        print(f'O maior número informado foi {mai}')
    else:
        print(f'Nenhum foi informado. Por tanto não ha números maiores!')
    print('-=' * 30)


from random import randint

maior(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),
      randint(0, 100), randint(0, 100))
maior(randint(0, 100), randint(0, 100), randint(0, 100))
maior(randint(0, 100), randint(0, 100))
maior(randint(0, 100))
maior()
