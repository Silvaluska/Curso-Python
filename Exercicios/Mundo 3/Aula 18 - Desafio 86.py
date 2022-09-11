'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[], [], []]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o número para [{l+1}, {c+1}]: ')))
print('-='*20)
print('A matriz formada é:')
for l in matriz:
    for c in l:
        print(f'[{c}]', end=' ')
    print()