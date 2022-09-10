'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
    – O nome com todas as letras maiúsculas e minúsculas.
    – Quantas letras ao todo (sem considerar espaços).
    – Quantas letras tem o primeiro nome.
'''
nome = input('Escreva seu nome completo: ').strip()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))
separado = nome.split()
print('O primeiro nome possui {} letras'.format(len(separado[0])))