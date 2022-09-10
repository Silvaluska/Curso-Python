'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print('-='*20)
print('VAMOS JOGAR UM JOGO DE PAR OU IMPAR?')
print('-='*20)
qtd = 0
while True:
    v = int(input('Digite um valor: '))
    p = input('Par ou Impar? [P/I]: ').strip().upper()[0]
    while p not in 'PI':
        p = input('Par ou Impar? [P/I]: ').strip().upper()[0]
    r = randint(0,10)
    t = r + v
    print('-='*30)
    if t%2 == 0 and p == 'P':
        print(f'Você jogou {v} e o Computador {r}. Total deu {t} que é PAR')
    elif t%2 != 0 and p == 'I':
        print(f'Você jogou {v} e o Computador {r}. Total deu {t} que é IMPAR')
    elif p == 'P':
        print(f'Você jogou {v} e o Computador {r}. Total deu {t} que é IMPAR')
        break
    elif p == 'I':
        print(f'Você jogou {v} e o Computador {r}. Total deu {t} que é PAR')
        break
    print('-='*30)
    print('Você ganhou, PARABÊNS')
    qtd +=1
print(f'GAME OVER! Você venceu {qtd} vezes')