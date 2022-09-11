'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.                                                                           
    B) A soma dos valores da terceira coluna.                                                                                      
    C) O maior valor da segunda linha.
'''
matriz = [[], [], []]
pares = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o número para [{l+1},{c+1}]: ')))
        if matriz[l][c]%2 == 0:
            pares.append(matriz[l][c])
print('-='*20)
print('A matriz formada é:')
for l in matriz:
    for c in l:
        print(f'[{c}]', end=' ')
    print('')
print('-='*20)
print(f'A soma de todos os valores pares é {sum(pares)}')
print(f'A soma de todos os números da 3ª coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')