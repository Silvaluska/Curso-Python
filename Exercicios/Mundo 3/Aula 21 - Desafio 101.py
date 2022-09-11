'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    from datetime import date
    h = date.today().year
    i = h - ano
    if 0 < i < 16:
        return f'Com {i} anos: Não vota'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos: Voto Opcional'
    elif i >= 18:
        return f'Com {i} anos: Voto Obrigatório'
    elif i < 0:
        return 'Você nem nasceu ainda desgraça'


print('-'*25)
v = voto(int(input('Ano de nascimento: ')))
print(v)