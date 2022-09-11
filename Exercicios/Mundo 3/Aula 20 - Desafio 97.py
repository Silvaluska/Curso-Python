'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
    Ex: escreva(‘Olá, Mundo!’)
    Saída:
    ~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~
'''
def escreva(msg):
    t = len(msg)
    print('~'*(t+4))
    print(f'  {msg}')
    print('~'*(t+4))


escreva('Gustavo Guanabara')
escreva('Curso de python no youtube')
escreva('CeV')