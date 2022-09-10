'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
print('{:^80}'.format('Vamos jogar jokenpô?'))
print('-='*40)
print('Regras:')
print('''No Janken-pon, os jogadores devem simultaneamente escolher entre pedra, papel ou 
tesoura. Então, os jogadores comparam e decidir quem ganhou, da seguinte forma:''')
print('    Pedra ganha da tesoura (amassando-a ou quebrando-a)')
print('    Tesoura ganha do papel (cortando-o)')
print('    Papel ganha da pedra (embrulhando-a)')
print('-='*40)

# Escolhas
esc = input('Escolha Pedra, Papel ou Tesoura: ').strip().lower() #Escolha do jogador
if esc == 'pedra':
    p = 0
elif esc == 'papel':
    p = 1
elif esc == 'tesoura':
    p = 2
from random import randint
import emoji
comp = ['pedra', 'papel', 'tesoura']
emo = [emoji.emojize(':oncoming_fist:'), emoji.emojize(':raised_hand:'), emoji.emojize(':victory_hand:')]
rand = randint(0, 2)#Escolha do computador
esccomp = comp[rand]
escemo = emo[rand]

# som
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('jokenpô.mp3')
pygame.mixer.music.play()
pygame.event.wait(1800)

# Comandos if e else
print('''\nJo
ken
Pô\n''')
if esc == esccomp:
    print('Eu escolhi {} {}'.format(esccomp.upper(), escemo))
    print('Isso foi um empate')
elif esc == 'pedra' and esccomp == 'tesoura' or esc == 'papel' and esccomp == 'pedra' or esc == 'tesoura' and esccomp == 'papel':
    print('Eu escolhi {} {}'.format(esccomp.upper(), escemo))
    print('{} {} ganha do {} {}'.format(esc.upper(), emo[p], esccomp.upper(), escemo))
    print('\033[32mVocê ganhou')
elif esc == 'pedra' and esccomp == 'papel' or esc == 'papel' and esccomp == 'tesoura' or esc == 'tesoura' and esccomp == 'pedra':
    print('Eu escolhi {} {}'.format(esccomp.upper(), escemo))
    print('{} {} perde para o {} {}'.format(esc.upper(), emo[p], esccomp.upper(), escemo))
    print('\033[31mVocê perdeu')
else:
    print('Você digitou errado')