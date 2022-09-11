'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaint(valor):
    v = input(valor)
    while True:
        if v.isnumeric() == True:
            return f'Você acabou de digitar o númeor {v}'
        else:
            print('\033[0:31mERRO! Digite um número inteiro\033[m')
            v = input(valor)


a = leiaint('Digite um número inteiro: ')
print(a)