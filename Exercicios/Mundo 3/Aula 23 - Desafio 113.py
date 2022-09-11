'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaint(valor):
    while True:
        try:
            v = int(input(valor))
        except KeyboardInterrupt:
            print('\033[0:31mO usuário preferiu não digitar nenhum valor\033[m')
            return 0
        except:
            print('\033[0:31mERRO! Digite um número inteiro\033[m')
        else:
            return v

def leiafloat(valor):
    while True:
        try:
            v = float(input(valor))
        except KeyboardInterrupt:
            print('\033[0:31mO usuário preferiu não digitar nenhum valor\033[m')
            return 0
        except:
            print('\033[0:31mERRO! Digite um número Real\033[m')
        else:
            return v


i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número Real: ')
print(f'O inteiro é {i} e o real é {f}')