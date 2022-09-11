'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram
cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
'''
lista = []
pessoas = {}
soma = cont = 0
while True:
    pessoas['Nome'] = input('Nome: ')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    cont += 1
    pessoas['Sexo'] = input('Sexo M/F: ').upper()
    while pessoas['Sexo'] not in 'MF':
        pessoas['Sexo'] = input('ERRO! Digite apenas M ou F: ')
    lista.append(pessoas.copy())
    r = input('Quer continuar S/N: ').upper()
    while r not in 'SN':
        r = input('ERRO! Digite apenas S ou N: ')
    if r == 'N':
        break
print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A média de idade é de {soma/cont}')
print('- As mulheres cadastradas foram:', end='')
for id in lista:
    if id['Sexo'] == 'F':
        print(f' {id["Nome"]}', end='; ')
print()
print('- Lista de pessoas que estão acima da média:')
for id in lista:
    if id['Idade'] > soma/cont:
        print(f'    Nome = {id["Nome"]}; Sexo = {id["Sexo"]}; Idade = {id["Idade"]}')
print('<< Encerrado >>')