def apurarVotos(candsGov, candsPres, govBrancos, presBrancos, govNulos, presNulos):
    """
    Apura os votos imprimindo-os no teminal.
    """
    apuracao = "\n\t\tApuração de votos\n\n* Candidatos a governador:"

    for cand in candsGov:
        nome = cand["nome"]
        qtdVotos = cand["qtdVotos"]
        apuracao += f"\n\tVotos do(a) candidato(a) {nome}: {qtdVotos}"

    apuracao += f"\n\tVotos em branco: {govBrancos}\n\tVotos nulos: {govNulos}"

    apuracao += "\n\n* Candidatos a presidente:"

    for cand in candsPres:
        nome = cand["nome"]
        qtdVotos = cand["qtdVotos"]
        apuracao += f"\n\tVotos do(a) candidato(a) {nome}: {qtdVotos}"

    apuracao += f"\n\tVotos em branco: {presBrancos}\n\tVotos nulos: {presNulos}"

    print(apuracao)
