'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*20)
for k,v in aluno.items():
    print(f'    - O {k} é igual a {v}')