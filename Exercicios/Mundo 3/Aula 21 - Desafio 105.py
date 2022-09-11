'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    – Quantidade de notas
    – A maior nota
    – A menor nota
    – A média da turma
    – A situação (opcional)
'''
def notas(*n, s=False):
    """
    Função que processa varios números e calcula a quantidade de itens, valor máximo, valor minimo, média e situação das notas.
    :param n: Notas do aluno
    :param s: Parametro para a escolha de salvar a situação do aluno ou não
    :return: Retorna um dicionário que contem todas as informações processadas
    """
    dic = {}
    dic['Quantidade'] = len(n)
    dic['Maximo'] = max(n)
    dic['Minimo'] = min(n)
    dic['Média'] = sum(n)/len(n)
    if s == True:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Bom'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'Razoavel'
        else:
            dic['Situação'] = 'Ruim'
    return dic


print(notas(10,3,4,s=True))
r = input('Quer mostrar o help da função S/N: ').strip().upper()
if r == 'S':
    help(notas)