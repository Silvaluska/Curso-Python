'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.'''
nome = input('Digite seu nome completo: ').strip()
sep = nome.split()
print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(sep[0]))
print('Ultimo nome: {}'.format(sep[-1]))