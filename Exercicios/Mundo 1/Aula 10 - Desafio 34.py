'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o
aumento é de 15%.'''
sala = float(input('Digite o valor do seu salário: '))
if sala > 1250:
    nsala = sala*1.1
    print('Seu novo salário vai ser R$ {:.2f}'.format(nsala))
else:
    nsala = sala*1.15
    print('Seu novo salário vai ser R$ {:.2f}'.format(nsala))