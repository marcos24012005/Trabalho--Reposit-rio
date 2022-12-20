import os
from Filme import Filme


def cadastrarFilme() -> Filme:
    limparTela()
    print("-------- Cadastro de Filmes --------")
    filme = Filme()
    filme.setNome(input('Nome: '))
    filme.setDiretor(input('Diretor: '))
    filme.setAno(int(input('Ano: ')))
    filme.setGenero(input('Genêro: '))
    filme.setAvaliacao(float(input('Avaliação: ')))

    return filme


def editarFilme() -> Filme:
    limparTela()
    print("-------- Edição de Filme --------")
    filme = Filme()
    filme.setId(int(input('Id: ')))
    filme.setNome(input('Nome: '))
    filme.setDiretor(input('Diretor: '))
    filme.setAno(int(input('Ano: ')))
    filme.setGenero(input('Genêro: '))
    filme.setAvaliacao(float(input('Avaliacao: ')))

    return filme


def excluirFilme():
    print("-------- Exclusão de Filme --------")
    limparTela()
    id = int(input('Id: '))
    return id


def selecionarFilme():
    limparTela()
    print("-------- Seleção de Filme --------")
    id = int(input('Id: '))
    return id


def exibirFilme(filme: Filme):
    print("-------- Filme --------")
    print(f"Id: {filme.getId()}")
    print(f"Nome: {filme.getNome()}")
    print(f"Preço: {filme.getDiretor()}")
    print(f"Quantidade: {filme.getAno()}")
    print(f"Genêro: {filme.getGenero()}")
    print(f"Avaliação: {filme.getAvaliacao()}")


def exibirFilmes(filmes):
    limparTela()
    print("---------------- Filmes ----------------")
    for filme in filmes:
        exibirFilme(filme)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()
