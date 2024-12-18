def notas(*num, sit=False):
    """
    VERIFICA AS NOTAS E A SITUAÇÃO DA CLASSE!
    :param num: várias notas podem ser adicionadas
    :param sit: Se é necessário mostrar a situação da sala
    :return: um dict() com o total de notas, maior nota, menor nota, média e de forma opcional a situação da sala
    """
    sala = {}
    sala['total'] = len(num)
    mai = men = 0
    for i, n in enumerate(num):
        if i == 0:
            mai = n
            men = n
        else:
            if n > mai:
                mai = n
            if n < men:
                men = n
    sala['maior'] = mai
    sala['menor'] = men
    med = sum(num) / len(num)
    sala['média'] = med
    if sit == True:
        if med >= 7:
            sala['situação'] = 'BOA'
        elif med < 5:
            sala['situação'] = 'RUIM'
        else:
            sala['situação'] = 'RAZOÁVEL'
    return sala


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(help(notas))
