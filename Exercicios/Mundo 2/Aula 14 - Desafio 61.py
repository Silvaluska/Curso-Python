'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma
PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
print('-='*20)
print('{:^40}'.format('10 Termos de uma PA'))
print('-='*20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c= 1
while c != 11:
    print(n, end=' → ')
    n += r
    c += 1
print('Acabou')