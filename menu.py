from telas import *
from persistencia import Persistencia


def menu():
    limparTela()
    print("-------- New Netflix --------")
    print("1 - Cadastrar Filme")
    print("2 - Editar Filme")
    print("3 - Excluir Filme")
    print("4 - Selecionar Filme")
    print("5 - Listar Filmes")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        filme = cadastrarFilme()
        persistencia.criar(filme)
        exibirMsg("Filme cadastrado com sucesso!")
    elif opcao == 2:
        filme = editarFilme()
        persistencia.editar(filme)
        exibirMsg("Filme editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluirFilme()
        persistencia.excluir(id)
        exibirMsg("Filme excluído com sucesso!")
    elif opcao == 4:
        id = selecionarFilme()
        filme = persistencia.selecionar(id)
        if filme == None:
            exibirMsg("Filme não encontrado!")
        else:
            exibirFilme(filme)
            travarTela()
    elif opcao == 5:
        filmes = persistencia.selecionar_todos()
        exibirFilmes(filmes)
    elif opcao == 6:
        break
