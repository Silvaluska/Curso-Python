'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial
'''
def fatorial(num,show=False):
    """
    A função executa o calculo de um fatorial
    :param num: Número que será fatorado
    :param show: True para mostrar como o calculo foi feito e False para mostrar apenas o valor do fatorial
    :return: Sem retorno
    """
    s = 1
    for c in range(num,1,-1):
        s *= c
        if show == True:
            print(f'{c} x ', end='')
            if c == 2:
                print(f'1 = ', end='')
    print(s)

num = int(input('Qual número você quer fatorar? '))
fatorial(num, True)
h = input('Quer mostrar o help da função S/N? ').strip().upper()
if h == 'S':
    help(fatorial)