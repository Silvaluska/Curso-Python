'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
         'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in lista:
    print(f'Na palavra {c} temos ', end='')
    for l in c:
        if l in 'AEIOU':
            print(l.lower(),end=' ')
    print('')