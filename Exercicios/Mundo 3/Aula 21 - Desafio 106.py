'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
def helplucas():
    from time import sleep
    print('\033[49:42m-=' * 12)
    print('Sistema de ajuda PyHelp')
    print('-=' * 12)
    while True:
        f = input('\033[mFunção ou biblioteca: ').strip()
        if f.upper() == 'FIM':
            print('\033[49:41m-='*5)
            print('Até logo!')
            print('-='*5)
            break
        print('\033[49:46m-='*(12+int(len(f)/2)))
        print(f'Acessando o manual de {f}')
        print('-='*(12+int(len(f)/2)))
        print('\033[m','\033[30:47m', end='')
        sleep(1)
        help(f)


helplucas()