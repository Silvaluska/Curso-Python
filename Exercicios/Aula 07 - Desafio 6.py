'''
Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
n = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(n, n*2, n*3, n**(1/2)))