class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

class serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada


vingadores = filme('meu filme', 2018, 160)
print(vingadores.nome)