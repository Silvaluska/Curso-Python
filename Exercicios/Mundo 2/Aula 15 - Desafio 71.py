'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('='*30)
print('{:^30}'.format('Banco Aletto'))
print('='*30)
d = int(input('Quanto você quer sacar?: '))
n = 0
c = 50
while True:
    if d >= c:
        d -= c
        n += 1
    else:
        if n > 0:
            print(f'Total de {n} notas de R$ {c}')
        n = 0
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        elif d == 0:
            break
print('-='*26, '\nObrigado por usar Aletto Bank, Tenha um otimo dia!!')