'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No
final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c+1}: ')))
print('-='*30)
print(f'Os valores digitados foram {lista}')
print(f'O maior valor é {max(lista)} e está na ', end='')
for n in range(0, len(lista)):
    if lista[n] == max(lista):
        print(f'{n+1}ª posição',end=', ')
print(f'\nO menor valor é {min(lista)} e está na ', end='')
for n in range(0, len(lista)):
    if lista[n] == min(lista):
        print(f'{n+1}ª posição',end=', ')