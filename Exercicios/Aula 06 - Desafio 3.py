'''Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
# print('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))