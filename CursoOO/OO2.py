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
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - {self.duracao} min - Likes: {self._likes}'

class serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - {self.temporada} Temporadas - Likes: {self._likes}'

class playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = filme('vingadores - guerra infinita', 2018, 160)
atlanta = serie('atlanta', 2018, 2)
tmep = filme('todo mundo em pânico', 1998, 120)
demolidor = serie('Demolidor', 2016, 3)
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

lista_programas = [vingadores, atlanta, demolidor, tmep]
lista_fds = playlist('Final de semana', lista_programas)
print(f'O tamanho da playlist é {len(lista_fds)}')

for programa in lista_programas:
    print(programa)

print(f'Tem demolidor {demolidor in lista_fds}')
