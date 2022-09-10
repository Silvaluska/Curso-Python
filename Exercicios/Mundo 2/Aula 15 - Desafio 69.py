'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.
'''
qtd18 = qtdm = qtd20f = 0
while True:
    print('-='*20)
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    idade = int(input('Idade: '))
    c = input('Quer continuar [S/N]: ').strip().upper()[0]
    if c not in 'SN':
        c = input('Quer continuar [S/N]: ').strip().upper()[0]
    if idade > 18:
        qtd18 += 1
    if sexo == 'M':
        qtdm += 1
    if sexo == 'F' and idade < 20:
        qtd20f += 1
    if c == 'N':
        print('-'*30)
        break
print(f'{qtd18} pessoas cadastradas possuem mais de 18 anos')
print(f'{qtdm} homens foram cadastrados')
print(f'{qtd20f} Mulheres acima de 20 anos foram cadastradas')