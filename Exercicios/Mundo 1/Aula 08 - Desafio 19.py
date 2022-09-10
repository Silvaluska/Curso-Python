'''
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
aln1 = input('Digite o nome do primeiro aluno: ')
aln2 = input('Digite o nome do segundo aluno: ')
aln3 = input('Digite o nome do terceiro aluno: ')
aln4 = input('Digite o nome do Quarto aluno: ')
from random import choice
n = choice([aln1, aln2, aln3, aln4])
print('O aluno sorteado foi {}'.format(n))