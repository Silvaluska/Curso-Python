'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = input('Digite uma frase: ').strip()
frase = frase.lower()
print('A frase possui {} vezes a letra A'.format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A ultima posição da letra A é {}'.format(frase.rfind('a')+1))