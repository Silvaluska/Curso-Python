'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
import datetime
h = datetime.date.today().year
pessoas = {}
pessoas['Nome'] = input('Nome: ')
pessoas['Idade'] = h - int(input('Ano de Nascimento: '))
pessoas['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoas['CTPS'] != 0:
    pessoas['Contrato'] = int(input('Ano de Contratação: '))
    pessoas['Salario'] = float(input('Salário: '))
    pessoas['Aposentadoria'] = 35 - (h - pessoas['Contrato'])
print('-='*30)
for k,v in pessoas.items():
    print(f'    - O {k} tem valor igual a {v}')