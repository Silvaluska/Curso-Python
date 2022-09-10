'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.
'''
print('-='*20, '\n{:^40}\n'.format('Loja Baratão'), '-='*20)
tg = ma1000 = nmaba = 0
maba = 0
while True:
    nome = input('Nome do produto: ').strip()
    preco = int(input('Preço: '))
    c = input('Quer continuar [S/N]: ').strip().upper()[0]
    while c not in 'SN':
        c = input('Quer continuar [S/N]: ').strip().upper()[0]
    print('-='*20)
    if tg == 0:
        maba = preco
    tg += preco
    if preco > 1000:
        ma1000 += 1
    if preco < maba:
        nmaba = nome
        maba = preco
    if c == 'N':
        print('-'*30)
        break
print(f'O total gasto foi de R$ {tg}')
print(f'{ma1000} Produtos custam mais de R$ 1000')
print(f'O nome do produto mais barato é {nmaba}')