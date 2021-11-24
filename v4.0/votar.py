from menus import menuVotacaoPosSelec, menuVotacaoPreSelec

def iniciarVotacao(candidatos, brancos, nulos):
    """
    Inicia o processo de votação.
    """
    menuVotacaoPreSelec()
    op = int(input(">>> Digite a sua opção: "))

    while True:
        if op == 1:
            numCand = int(input("\n>>> Informe o número de seu candidato: "))
            
            for candidato in candidatos:
                if numCand == candidato[0]:
                    nomeCand = candidato[1]
                    menuVotacaoPosSelec(nomeCand)
                    opc = int(input(">>> Digite a sua opção: "))

                    while True:
                        if opc == 1:
                            print("\n[*] Voto confirmado.")
                            return 'confirma', numCand

                        elif opc == 2:
                            brancos += 1
                            print("\n[*] Voto em branco confirmado.")
                            return 'branco', brancos

                        elif opc == 3:
                            nulos += 1
                            print("\n[*] Voto anulado.")
                            return 'nulo', nulos

                        else:
                            print("\n[!] Opção inválida.")
                            menuVotacaoPosSelec(nomeCand)
                            opc = int(input(">>> Digite a sua opção: "))

            print("\n[!] Candidato não encontrado.")
            anular = input("\n>>> Deseja anular o voto? [s/n]: ")

            if anular == "s":
                nulos += 1
                print("\n[*] Voto anulado.")
                return "nulo", nulos

            elif anular == "n":
                op = 1

            else:
                op = 0

        elif op == 2:
            brancos += 1
            print("\n[*] Voto em branco confirmado.")
            return 'branco', brancos

        elif op == 3:
            nulos += 1
            print("\n[*] Voto anulado.")
            return 'nulo', nulos

        else:
            print("\n[!] Opção inválida.")
            menuVotacaoPreSelec()
            op = int(input(">>> Digite a sua opção: "))
