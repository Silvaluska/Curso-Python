def metade(n, m=False):
    if m == True:
        return moeda(n/2)
    else:
        return n/2


def dobro(n, m=False):
    if m == True:
        return moeda(n*2)
    else:
        return n*2


def aumentar(n, p, m=False):
    if m == True:
        return moeda(n*(1+p/100))
    else:
        return n*(1+p/100)


def diminuir(n, p, m=False):
    if m == True:
        return moeda(n*(1-p/100))
    else:
        return n*(1-p/100)


def moeda(n):
    return f'{n:.2f}'.replace('.',',')


def resumo(n, a, d):
    print('-'*28)
    print(f'{"Resumo de valor":^28}')
    print('-'*28)
    print(f'{"Preço analisado:":20}{moeda(n)}')
    print(f'{"Dobro do preço:":20}{dobro(n,True)}')
    print(f'{"Metade do preço:":20}{metade(n, True)}')
    print(f'{a}{"% de aumento:":18}{aumentar(n, a, True)}')
    print(f'{d}{"% de redução:":18}{diminuir(n, d, True)}')
    print('-' * 28)