'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Chapecoense.
'''
times = 'Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional', 'Atlético-MG', 'Bragantino', 'Santos', 'América-MG', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará SC', 'Coritiba', 'Avai', 'Fortaleza', 'Cuiabá', 'Atlético-GO', 'Juventude'
print('{:^40}'.format('Tabela do brasileirão'))
print('*'*40, f'\nOs 5 primeiros colocados do brasileirão são {times[:5]}')
print('*'*40, f'\nOs ultimos 4 colocados do brasileirão são {times[-4:]}')
print('*'*40, '\nOs times do brasileirão em ordem alphabetica é')
print(sorted(times))
print('*'*40, f'\nO time do internacional está na {times.index("Internacional")+1}ª posição')