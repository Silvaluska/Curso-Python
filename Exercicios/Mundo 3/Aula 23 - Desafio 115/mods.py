def cabecalho(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


def titulo():
    cabecalho('MENU PRINCIPAL')
    print('\033[0:34m1 - Ver pessoas cadastradas\033[m')
    print('\033[0:34m2 - Cadastrar nova pessoa\033[m')
    print('\033[0:34m3 - Sair do sistema\033[m')
    print('-'*40)


def cadastro(nome):
    cabecalho('PESSOAS CADASTRADAS')
    lerArq(nome)
    print('-' * 40)


def cadastrar(nome):
    n = input('\033[0:31mNome: ')
    i = int(input('Idade: '))
    try:
        a = open(nome, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo {nome}')
    else:
        try:
            a.write(f'{n:30}{i} anos\n')
        except:
            print(f'Houve um erro ao colocar o dados no arquivo {nome}')
        else:
            print(f'Novo registro de {n} adicionado\033[m')


def opcao(msg):
    while True:
        try:
            op = leiaint(msg)
        except:
            print('Opção invalida')
        else:
            return op


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


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro')
    else:
        print('Arquivo de cadastro criado')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        print(a.read())
    finally:
        a.close()