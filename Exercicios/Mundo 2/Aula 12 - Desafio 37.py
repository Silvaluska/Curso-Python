'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão')
print('[0] Converter para binário\n[1] Converter para octogonal\n[2] Converter para hexadecimal')
fator = int(input('Qual é a sua escolha: '))
if fator == 0:
    bina = bin(num)[2:]
    print('O númeuro {} em binário é {}'.format(num, bina))
elif fator == 1:
    octogonal = oct(num)[2:]
    print('O número {} em octogonal é {}'.format(num, octogonal))
elif fator == 2:
    hexa = hex(num)[2:]
    print('O número {} em hexadecimal é {}'.format(num, hexa))
else:
    print('Você é burro pra cacete não consegue nem seguir uma ordem de digitar um número entre de 0 a 2')