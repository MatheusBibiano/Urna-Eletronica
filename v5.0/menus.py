def menuUrna():
    """
    Imprime o menu com as opções disponíveis no terminal.
    """
    MENU = """
    +----------- Urna Eletrônica 5.0 -----------+
    |                                           |
    | [1] Listar candidatos.                    |
    | [2] Iniciar votação.                      |
    | [3] Apurar votos.                         |
    | [4] Desligar a urna.                      |
    |                                           |
    +-------------------------------------------+
    """
    print(MENU)


def menuVotacaoPreSelec():
    """
    Imprime o menu de votação com o nome
    do candidato correspondente no terminal.
    """
    MENU = """
        +-------------------------+
        |                         |
        | [1] Escolher candidato. |
        | [2] Votar em branco.    |
        | [3] Anular voto.        |
        |                         |
        +-------------------------+
    """
    print(MENU)


def menuVotacaoPosSelec(nomeCand):
    """
    Imprime o menu de votação com o nome
    do candidato correspondente no terminal.
    """
    MENU = f"""
        Candidato: {nomeCand}
        +-----------------------+
        |                       |
        | [1] Confirmar voto.   |
        | [2] Votar em branco.  |
        | [3] Anular voto.      |
        |                       |
        +-----------------------+
    """
    print(MENU)
