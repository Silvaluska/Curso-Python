'''
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
'''
from time import sleep
import mods

if not mods.arqExiste('cursoemvideo.txt'):
    mods.criarArq('cursoemvideo.txt')

while True:
    mods.titulo()
    op = mods.opcao('Escolha sua opção: ')
    if op == 1:
        mods.cadastro('cursoemvideo.txt')
    elif op == 2:
        mods.cadastrar('cursoemvideo.txt')
    elif op == 3:
        mods.cabecalho('SAINDO DO SISTEMA... ATÉ LOGO!')
        break
    else:
        print('\033[0:31mOpção inválida\033[m')
    sleep(1.5)