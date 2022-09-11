'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
'''
alunos = []
while True:
    aluno = []
    aluno.append(input('Nome: '))
    aluno.append(int(input('Nota 01: ')))
    aluno.append(int(input('Nota 02: ')))
    alunos.append(aluno[:])
    aluno.clear()
    r = input('Quer continuar S/N: ').strip().upper()
    if r == 'N':
        break
print(f'{"Boletim":^30}')
print('-'*30)
print('nª     nome     média')
for a in alunos:
    print(f'{alunos.index(a):<7}{a[0]:<10}{(a[1]+a[2])/2}')
while True:
    print('-'*30)
    v = int(input('Mostrar a nota de qual alunos? '))
    if v == 999:
        break
    print(f'Notas de {alunos[v][0]} são {alunos[v][1]} e {alunos[v][2]}')
print('Programa Finzalidado')