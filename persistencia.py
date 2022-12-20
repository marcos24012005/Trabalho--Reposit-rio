from json_storage import JsonStorage
from Filme import Filme


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Filme) -> Filme:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado.toDict())
        self.__storage.gravarJson(dados)

    def editar(self, dado: Filme) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado.toDict()
        self.__storage.gravarJson(dados)

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
        self.__storage.gravarJson(dados)

    def selecionar(self, id: int) -> Filme and None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                return dado
        return None

    def selecionar_todos(self) -> list:
        filmes = []
        for i in self.__storage.lerJson():
            filme = Filme()
            filme.setId(i['id'])
            filme.setNome(i['nome'])
            filme.setDiretor(i['diretor'])
            filme.setAno(i['ano'])
            filme.setGenero(i['genero'])
            filme.setAvaliacao(i['avaliacao'])
            filmes.append(filme)
        return filmes

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1
