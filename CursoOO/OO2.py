class filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao

    @property
    def nome(self):
        return self.__nome.title()

vingadores = filme('meu filme', 2018, 160)
print(vingadores.nome)