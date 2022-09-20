import os
from Conex import Conexao
from time import sleep

banco = Conexao('localhost', 'vasp', 'postgres', '123')


def limpar_tela():
    """Funcao que limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def boas_vindas():
    """funcao que faz o login de um usuario no sistema e retorna seu nome, senha e seu id"""
    while True:
        limpar_tela()
        print("Bem Vindo a WIKI FANDOM VASP !\n\n")
        nome_do_usuario = input("Digite o NickName do Usuario: ")
        senha = input("Digite a senha: ")

        entrada = banco.consultar(
                "SELECT Nickname, Senha, Identificacao FROM Usuario WHERE Nickname='" + nome_do_usuario + "' AND Senha='" + senha + "'")
        if entrada:
            break
        else:
            print("NickName ou Senha incorretos !")
            sleep(1)


    return nome_do_usuario, senha, entrada[0][2]


def eh_Adm(nome_do_usuario, senha):
    """Funcao que recebe o nome_do_usuario e a senha e verifica se o usuario
    com essas credenciais eh um Administrador"""
    if banco.consultar(
            "SELECT * FROM Usuario AS U JOIN Administrador AS Adm ON U.Identificacao=Adm.Identificacao AND U.Nickname='"
            + nome_do_usuario + "' AND U.Senha='" + senha + "'"):
        return True
    else:
        False


def eh_Colaborador(nome_do_usuario, senha):
    """Funcao que recebe o nome_do_usuario e a senha e verifica se o usuario
        com essas credenciais eh um Colaborador"""
    if banco.consultar(
            "SELECT * FROM Usuario AS U JOIN Colaborador AS Col ON U.Identificacao=Col.Identificacao AND U.Nickname='"
            + nome_do_usuario + "' AND U.Senha='" + senha + "'"):
        return True
    else:
        False


def deletar_usuario():
    """Funcao que deleta um usuario do banco de dados"""
    while True:
        limpar_tela()
        usuarios = banco.consultar("SELECT Nickname FROM Usuario")

        if usuarios is None:
            print("Sem Usuarios para deletar !")
            sleep(1)
            break

        print("Vamos deletar qual Usuario?")
        print(usuarios)
        resposta = input()

        if resposta not in [user[0] for user in usuarios]:
            print("Usuario inexistente !")
            sleep(1)
            break
        else:
            if banco.manipular("DELETE FROM Usuario WHERE Nickname='" + resposta + "'"):
                print("Usuario deletado com Sucesso !")
                sleep(1)
            else:
                print("Erro ao deletar Usuario !")
                sleep(1)


def deletar_comunidade():
    """Funcao que deleta uma comunidade do banco de dados"""
    while True:
        limpar_tela()
        comunidades = banco.consultar("SELECT Identificacao FROM Comunidade")

        if comunidades is None:
            print("Sem comunidades para deletar !")
            sleep(1)
            break

        print("Vamos deletar qual Comunidade?")
        print(comunidades)
        resposta = input()

        if resposta not in [str(comunidade[0]) for comunidade in comunidades]:
            print("Comunidade inexistente !")
            sleep(1)
            break
        else:
            if banco.manipular("DELETE FROM Comunidade WHERE Identificacao='" + resposta + "'"):
                print("Comunidade deletada com Sucesso !")
                sleep(1)
            else:
                print("Erro ao deletar Comunidade !")
                sleep(1)


def adicionar_usuario():
    """Funcao que adiciona um usuario no banco de dados"""
    while True:
        limpar_tela()
        print("Vamos adicionar um Usuario")

        nome_do_usuario = input("Digite o NickName do Usuario: ")
        senha = input("Digite a senha: ")
        id = input("Digite a Identificacao: ")

        if banco.manipular(
                "INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('" + nome_do_usuario + "', '" + senha + "', '" + id + "')"):
            print("Usuario Inserido com Sucesso !")
            sleep(1)
        else:
            print("Erro ao inserir o usuario !")
            sleep(1)
            break


def adicionar_comunidade():
    """Funcao que adiciona uma comunidade no banco de dados"""
    while True:
        limpar_tela()
        print("Vamos adicionar uma Comunidade")

        numero_de_seguidores = input("Digite o Numero de Seguidores: ")
        numero_de_leitores = input("Digite o Numero de Leitores: ")
        id = input("Digite a Identificacao: ")

        if banco.manipular(
                "INSERT INTO Comunidade(Seguidores, Numero_de_leitores, Identificacao) VALUES ('" + numero_de_seguidores + "', '" + numero_de_leitores + "','" + id + "')"):
            print("Comunidade Inserida com Sucesso !")
            sleep(1)
        else:
            print("Erro ao inserir o comunidade !")
            sleep(1)
            break


def atualizar_usuario():
    """Funcao que atualiza um usuario existente no banco de dados"""
    while True:
        limpar_tela()
        usuarios = banco.consultar("SELECT Nickname FROM Usuario")

        if usuarios is None:
            print("Sem Usuarios para Atualizar !")
            sleep(1)
            break

        print("Vamos Atualizar qual Usuario?")
        print(usuarios)
        resposta = input()

        if resposta not in [user[0] for user in usuarios]:
            print("Usuario inexistente !")
            sleep(1)
            break
        else:
            nome_do_usuario = input("Digite novo NickName do Usuario: ")
            senha = input("Digite a nova senha: ")

            if banco.manipular(
                    "UPDATE Usuario SET Nickname='" + nome_do_usuario + "' , Senha='" + senha + "' WHERE Nickname='" + resposta + "'"):
                print("Usuario Atualizado com Sucesso !")
                sleep(1)
            else:
                print("Erro ao Atualizar o usuario !")
                sleep(1)
                break


def virarAdm():
    """Funcao que permite que um Usuario vire um Administrador"""
    while True:
        limpar_tela()
        usuarios = banco.consultar("SELECT Nickname, Identificacao FROM Usuario")

        if usuarios is None:
            print("Sem Usuarios para Virar ADM !")
            sleep(1)
            break

        print("Qual usuario irá virar adm?")
        print(usuarios)
        resposta = input()

        if resposta not in [user[0] for user in usuarios]:
            print("Usuario inexistente !")
            sleep(1)
            break
        else:
            id = [user[1] for user in usuarios if user[0] == resposta]
            id = str(id[0])

            if banco.manipular(
                    "INSERT INTO Administrador(Identificacao) VALUES ('" + id + "')"):
                print("Administrador Inserido com Sucesso !")
                sleep(1)
            else:
                print("Erro ao Inserir o Adm !")
                sleep(1)
                break


def virarColaborador():
    """Funcao que permite que um Usuario vire um Colaborador"""
    while True:
        limpar_tela()
        usuarios = banco.consultar("SELECT Nickname, Identificacao FROM Usuario")

        if usuarios is None:
            print("Sem Usuarios para Virar Colaborador !")
            sleep(1)
            break

        print("Qual usuario irá virar Colaborador?")
        print(usuarios)
        resposta = input()

        if resposta not in [user[0] for user in usuarios]:
            print("Usuario inexistente !")
            sleep(1)
            break
        else:
            id = [user[1] for user in usuarios if user[0] == resposta]
            id = str(id[0])

            if banco.manipular(
                    "INSERT INTO Colaborador(Identificacao) VALUES ('" + id + "')"):
                print("Colaborador Inserido com Sucesso !")
                sleep(1)
            else:
                print("Erro ao Inserir o Adm !")
                sleep(1)
                break


def menu_adm(nome_do_usuario):
    """Funcao que recebe o nome de um Administrador e
     imprime o menu de opções do mesmo"""
    while True:
        limpar_tela()
        print(f'Bem Vindo Administrador {nome_do_usuario} !')
        print("[0]- Sair")
        print("[1]- Deletar Usuario")
        print("[2]- Deletar Comunidade")
        print("[3]- Adicionar Usuario")
        print("[4]- Adicionar Comunidade")
        print("[5]- Atualizar Usuario")
        print("[6]- Usuario Vira Administrador")
        print("[7]- Usuario Vira Colaborador")
        # print("[6]- Associar Comunidade a um Entretenimento")
        resposta = input()

        if resposta == "0":
            break
        elif resposta == "1":
            deletar_usuario()
        elif resposta == "2":
            deletar_comunidade()
        elif resposta == "3":
            adicionar_usuario()
        elif resposta == "4":
            adicionar_comunidade()
        elif resposta == "5":
            atualizar_usuario()
        elif resposta == "6":
            virarAdm()
        else:
            virarColaborador()


def interagir_personagem(personagem, identificador_colaborador):
    """Funcao que recebe um personagem e um identificador do colaborador
    e imprime os dados do personagem, e os comentarios da comunidade sobre ele
    assim como permite que o colaborador faça comentario nessa mesma comunidade"""
    while True:
        limpar_tela()
        #imprimir dados do personagem
        print("Tela do Personagem")
        print("ID:", personagem[4])
        print("Nome:", personagem[1])
        print("Idade:", personagem[3])
        print("Historia:", personagem[0])
        print("Habilidade:", personagem[2])

        #imprimir comentarios sobre o personagem
        comentarios = banco.consultar("SELECT IdentificacaoInterageColaborador, DataComentario, Comentario  FROM Postagem WHERE IdentificacaoInterageComunidade='" + str(personagem[4]) + "'" )

        if comentarios is None:
            print("Ainda não tem nenhum comentário !")
        else:
            print("\nComentários sobre o personagem", personagem[1], "na WIKI:")
            for comentario in comentarios:
                nome_do_comentador = banco.consultar(
                    "SELECT Nickname FROM Usuario WHERE Identificacao='" + str(comentario[0]) + "'")[0]
                print(nome_do_comentador, ":", comentario[2], "-", comentario[1])

        print("Digite um comentário: ")
        resposta = input()

        print("Digite um ID: ")
        id = input()

        if banco.manipular(
                "INSERT INTO Postagem(IdentificacaoInterageColaborador, IdentificacaoInterageComunidade, IdentificacaoPostagem, DataComentario,Comentario) VALUES ('" + str(identificador_colaborador)+ "', '" + str(personagem[4]) + "', '" + id + "', NOW(), '" + resposta + "')"):
            print("Postagem inserida com Sucesso")
            sleep(1)
        else:
            print("Erro ao Inserir o Comentario !")
            sleep(1)
            break


def interagir_personagens(personagens, id):
    """ Funcao que recebe uma lista de personagens
    que foram lidos do banco de dados e o id do colaborador que
    ira interagir com algum personagem, e permite o Colaborador
    a escolher o Personagem que ele irá interagir"""
    while True:
        limpar_tela()

        if personagens is None:
            print("Sem Personagens para Interagir !")
            sleep(1)
            break

        print("Qual a interacao sera com qual Personagem?")
        print(personagens)
        resposta = input()

        if resposta not in [str(personagem[4]) for personagem in personagens]:
            print("Personagem inexistente !")
            sleep(1)
            break
        else:
            interagir_personagem([personagem for personagem in personagens if resposta == str(personagem[4])][0], id)


def interagir(id):
    """ Funcao que recebe  o id do colaborador que
        ira interagir com alguma Comunidade, lista as comunidades que
        eh possivel de interagir, e permite o Colaborador
        a escolher o tipos de comunidade que sera realizada a interacao:
        filmes, series, cenario, quadrinhos ou personagens."""
    while True:
        limpar_tela()

        filmes = banco.consultar("SELECT * FROM Filme")
        series = banco.consultar("SELECT * FROM Serie")
        cenarios = banco.consultar("SELECT * FROM Cenario")
        quadrinhos = banco.consultar("SELECT * FROM Quadrinho")
        personagens = banco.consultar("SELECT * FROM Personagem")

        if (filmes, series, cenarios, quadrinhos, personagens) == (None, None, None, None, None):
            print("Sem comunidades para Interagir !")
            sleep(1)
            break

        print("Vamos Interagir com qual Comunidade?")

        print("[0]- Sair")
        print("[1]- Filmes: ", filmes)
        print("[2]- Series: ", series)
        print("[3]- Cenarios: ", cenarios)
        print("[4]- Quadrinhos: ", quadrinhos)
        print("[5]- Personagens: ", personagens)

        resposta = input()

        if resposta == "0":
            break
        elif resposta == "5":
            interagir_personagens(personagens, id)
        """ elif resposta == "1":
            # interagir_filmes(filmes)
            pass
        elif resposta == "2":
            # interagir_series(series)
            pass
        elif resposta == "3":
            # interagir_cenarios(cenarios)
            pass
        elif resposta == "4":
            # interagir_quadrinhos(quadrinhos)
            pass"""



def menu_colaborador(nome_do_usuario, id):
    """Funcao que recebe o nome de um Colaborador e seu ID e
        imprime o menu de opções do mesmo"""
    while True:
        limpar_tela()
        print(f'Bem Vindo Colaborador {nome_do_usuario} !')
        print("[0]- Sair")
        print("[1]- Interagir")

        resposta = input()

        if resposta == "0":
            break
        else:
            interagir(id)


def login():
    """Funcao que faz o login de um usuario no sistema
    atraves da funcao boas vinda e a conferencia se
    o mesmo eh um Administrador ou um Colaborador"""
    nome_do_usuario, senha, id = boas_vindas()

    if eh_Adm(nome_do_usuario, senha):
        menu_adm(nome_do_usuario)

    elif eh_Colaborador(nome_do_usuario, senha):
        menu_colaborador(nome_do_usuario, id)


def main():
    """Funcao do Menu principal (Login)"""
    while True:
        limpar_tela()

        print("Digite: ")
        print("[0]- Sair")
        print("[1]- Login")
        resposta = input()

        if resposta == "0":
            print("Ate mais !")
            break
        else:
            login()

if __name__ == "__main__":
    main()
    banco.fechar()

"""def assciar_filme_a_comunidade(comunidade):
    while True:
        limpar_tela()
        filme = banco.consultar("SELECT Nome FROM Midia JOIN Filme")

        if filme is None:
            print("Sem Filme para Associar !")
            sleep(1)
            break

        print("Vamos Associar qual filme?")
        print(filme)
        resposta = input()

        if resposta not in filme:
            print("Filme inexistente !")
            sleep(1)
            break
        else:
            nome_do_usuario = input("Digite novo NickName do Usuario: ")
            senha = input("Digite a nova senha: ")

            if banco.manipular(
                    "UPDATE Usuario SET Nickname='" + nome_do_usuario + "' Senha='" + senha + "'"):
                print("Usuario Atualizado com Sucesso !")
                sleep(1)
            else:
                print("Erro ao Atualizar o usuario !")
                sleep(1)

def associar_comunidade_a_entre2(comunidade):
    while True:
        limpar_tela()
        print("Vamos Associar a Comunidade", comunidade, "a qual Entretenimento?")

        print("[0]- Sair")
        print("[1]- Filme")
        print("[2]- Serie")
        print("[3]- Personagem")
        print("[4]- Quadrinho")
        print("[5]- Cenario")
        resposta = input()

        if resposta == "0":
            break
        elif resposta == "1":
            pass
        elif resposta == "2":
            pass
        elif resposta == "3":
            pass
        elif resposta == "4":
            pass
        elif resposta == "5":
            pass
        else:
            pass

def associar_comunidade_a_entre():
    while True:
        limpar_tela()
        comunidades = banco.consultar("SELECT Identificacao FROM Comunidade")

        if comunidades is None:
            print("Sem comunidades para Associar !")
            sleep(1)
            break

        print("Vamos Associar qual Comunidade?")
        print(comunidades)
        resposta = input()

        if resposta not in comunidades:
            print("Comunidade inexistente !")
            sleep(1)
            break
        else:
            associar_comunidade_a_entre2(resposta)"""
