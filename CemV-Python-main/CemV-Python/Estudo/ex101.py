def voto(nas):
    """MInha PICa"""
    from datetime import datetime
    idade = datetime.now().year - nas
    if idade >= 65 or 16 < idade < 18:
        sit = 'OPCIONAL'
    elif 18 <= idade < 65:
        sit = 'OBRIGATÓRIO'
    elif idade < 16:
        sit = 'NÃO VOTA'
    return print(f'Com {idade}. {sit}')


n = int(input('Ano de nascimento: '))
voto(n)
