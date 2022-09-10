'''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''
cidade = input('Digite o nome da sua cidade: ').strip()
cidade2 = cidade.lower().split()
print('O nome da sua cidade começa com Santo? {}'.format('santo' in cidade2[0]))