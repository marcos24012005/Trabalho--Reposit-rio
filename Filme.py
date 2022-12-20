class Filme():
    __id: int
    __nome: str
    __diretor: str
    __ano: int
    __genero: str
    __avaliacao: float

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getDiretor(self):
        return self.__diretor

    def setDiretor(self, diretor):
        self.__diretor = diretor

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getAvaliacao(self):
        return self.__avaliacao

    def setAvaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    def toDict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'diretor': self.__diretor,
            'ano': self.__ano,
            'genero': self.__genero,
            'avaliacao': self.__avaliacao
        }
