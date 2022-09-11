'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''
grupo = [[], []]
while True:
    grupo[0].append(input('Nome: '))
    grupo[1].append(int(input('Peso: ')))
    r = input('Quer continuar S/N: ').upper().strip()
    if r == 'N':
        break
print(f'{len(grupo[0])} pessoas foram cadastradas')
print(f'O maior peso foi {max(grupo[1])} Kg. Peso de ', end='')
for p in grupo[1]:
    if p == max(grupo[1]):
        print(f'{grupo[0][grupo[1].index(p)]}', end=', ')
print(f'\nO menor peso foi {min(grupo[1])} Kg. Peso de ', end='')
for p in grupo[1]:
    if p == min(grupo[1]):
        print(f'{grupo[0][grupo[1].index(p)]}', end=', ')