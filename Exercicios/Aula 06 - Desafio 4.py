'''
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.
'''
algo = input('Digite algo: ')
print('o tipo primitivo desse valor é: ', type(algo))
print('O que você digitou é alfanumerico? ', algo.isalnum())
print('O que você digitou é alfabético? ', algo.isalpha())
print('O que você digitou é Ascii? ', algo.isascii())
print('O que você digitou é digit? ', algo.isdigit())
print('O que você digitou esta escrito em minusculo? ', algo.islower())
print('O que você digitou é Decimal? ', algo.isdecimal())
print('O que você digitou é um indentificador valido? ', algo.isidentifier())
print('O que você digitou é número? ', algo.isnumeric())
print('O que você digitou é possivel de ser impresso? ', algo.isprintable())
print('O que você digitou só tem espaços? ', algo.isspace())
print('O que você digitou está capitalizada? ', algo.istitle())
print('O que você digitou está escrito em maiusculo? ', algo.isupper())