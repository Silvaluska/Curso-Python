'''
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''
nome = input('Digite seu nome completo: ').strip()
nome = nome.lower()
print('Seu nome possui Silva? {}'.format('silva' in nome))