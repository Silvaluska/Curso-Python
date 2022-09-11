'''
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
import requests
try:
    requests.get('http://pudim.com.br/')
except:
    print('\033[0:31mNão consegui acessar o site do pudim\033[m')
else:
    print('\033[0:32mConsegui acessar o site do pudim com SUCESSO!\033[m')