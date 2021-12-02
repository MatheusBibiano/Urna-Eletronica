def listarCandidatos(candsGov, candsPres):
    """
    Lista os candidatos(as) a governador e presidente no terminal.
    """
    listaCandidatos = "\n* Lista de candidatos a governador:"

    for cand in candsGov:
        num = cand["num"]
        nome = cand["nome"]
        listaCandidatos += f"\n\tCandidato(a) {num}: {nome}"

    listaCandidatos += "\n\n* Lista de candidatos à presidência:"

    for cand in candsPres:
        num = cand["num"]
        nome = cand["nome"]
        listaCandidatos += f"\n\tCandidato(a) {num}: {nome}"

    print(listaCandidatos)
    