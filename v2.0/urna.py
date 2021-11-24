# -*- coding: utf-8 -*-
# Desenvolvido por: Matheus Bibiano & Matheus Cereda


# Variáves com os nome dos candidatos a presidente.
nomePres1 = "PRESIDENTE-1"
nomePres2 = "PRESIDENTE-2"
nomePres3 = "PRESIDENTE-3"
nomePres4 = "PRESIDENTE-4"
nomePres5 = "PRESIDENTE-5"

# Variáveis com os nomes dos candidatos a governador.
nomeGov1 = "GOVERNADOR-1"
nomeGov2 = "GOVERNADOR-2"
nomeGov3 = "GOVERNADOR-3"
nomeGov4 = "GOVERNADOR-4"
nomeGov5 = "GOVERNADOR-5"

# Variáveis que armazenam a quantidade
# de votos de cada condidato a presidente.
votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0

# Variáveis que armazenam a quantidade
# de votos de cada condidato a governador.
votoGov1 = 0
votoGov2 = 0
votoGov3 = 0
votoGov4 = 0
votoGov5 = 0

# Variáveis que armazenam o total de votos
# nulos e brancos para candidatos a governador e presidente.
votoPresNulo = 0
votoPresBranco = 0
votoGovNulo = 0
votoGovBranco = 0

# Menu principal da urna.
print("\n\n+----------- Urna Eletrônica 2.0 -----------+\n\
    \r|                                           |\n\
    \r| [1] Listar candidatos.                    |\n\
    \r| [2] Iniciar votação.                      |\n\
    \r| [3] Apurar votos.                         |\n\
    \r| [4] Desligar a urna.                      |\n\
    \r|                                           |\n\
    \r+-------------------------------------------+\n\
    \r|\
")

# Variável reposável por armazenar
# a opção escolhida pelo usuário.
op = int(input("+--> Digite a sua opção: "))

while 0 < op <= 4:
    if op == 1:
        print(f"\n\n\
            \r * Lista de candidatos a governador:\n\
            \r   Candidato(a) 1: {nomeGov1}\n\
            \r   Candidato(a) 2: {nomeGov2}\n\
            \r   Candidato(a) 3: {nomeGov3}\n\
            \r   Candidato(a) 4: {nomeGov4}\n\
            \r   Candidato(a) 5: {nomeGov5}\n\
            \n\
            \r * Lista de candidatos à presidência:\n\
            \r   Candidato(a) 1: {nomePres1}\n\
            \r   Candidato(a) 2: {nomePres2}\n\
            \r   Candidato(a) 3: {nomePres3}\n\
            \r   Candidato(a) 4: {nomePres4}\n\
            \r   Candidato(a) 5: {nomePres5}\n\
        ")

    elif op == 2:

        #----------------- LÓGICA DE VOTAÇÃO PARA GOVERNADOR -----------------

        # Variável responsável por armazenar o número
        # do candidato a governador escolhido.
        numCandGov = int(input('\n>>> Informe o número de seu candidato a governador: '))

        # While responsável por repetir a
        # entrada acima, caso o usuário digite
        # um candidato inválido.
        while True:
            if numCandGov == 1:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomeGov1}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoGov1 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomeGov1}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 2:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomeGov2}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoGov2 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomeGov2}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 3:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomeGov3}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoGov3 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomeGov3}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 4:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomeGov4}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoGov4 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomeGov4}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 5:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomeGov5}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoGov5 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomeGov5}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break
            
            else:
                print('\n[!] Opção Inválida.')

                # Variável responsável por armazenar o número
                # do candidato a governador escolhido.
                numCandGov = int(input('\n>>> Informe o número de seu candidato a governador: '))



        #----------------- LÓGICA DE VOTAÇÃO PARA PRESIDENTE -----------------

        # Variável responsável por armazenar o número
        # do candidato a presidente escolhido.
        numCandPres = int(input('\n>>> Informe o número de seu candidato a presidente: '))

        # While responsável por repetir a
        # entrada acima, caso o usuário digite
        # um candidato inválido.
        while True:
            if numCandPres == 1:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomePres1}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoPres1 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomePres1}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 2:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomePres2}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoPres2 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomePres2}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 3:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomePres3}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoPres3 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomePres3}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 4:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomePres4}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoPres4 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomePres4}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 5:
                # Menu de votação.
                print(f"\n\
                    \r Nome: {nomePres5}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                # Variável reposável por armazenar
                # a opção escolhida pelo usuário.
                op = int(input("+--> Digite a sua opção: "))

                # While para repetir o menu de votação caso seja necessário.
                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            # O voto é confirmado e contabilizado para o candito.
                            votoPres5 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            # O voto é confirmado e contabilizado para voto em branco.
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            # O voto é confirmado e contabilizado para voto nulo.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        # Variável responsável por armazenar a escolha do usuário.
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            # O voto é anulado e contabilizado.
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            # O menu de votação se repete para que
                            # o usuário selecione outra opção.
                            print(f"\n\
                                \r Nome: {nomePres5}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            # Variável reposável por armazenar
                            # a opção escolhida pelo usuário.
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break
            
            else:
                print('\n[!] Opção Inválida.')

                # Variável responsável por armazenar o número
                # do candidato a presidente escolhido.
                numCandPres = int(input('\n>>> Informe o número de seu candidato a presidente: '))

    
    elif op == 3:
        # Imprime a apuração baseada em todos os votos realizados.
        print(f"\n\n\
            \r             Apuração de votos\n\
            \r\n * Candidatos a governador:\n\
            \r   Votos do(a) candidato(a) {nomeGov1}:  {votoGov1}\n\
            \r   Votos do(a) candidato(a) {nomeGov2}:  {votoGov2}\n\
            \r   Votos do(a) candidato(a) {nomeGov3}:  {votoGov3}\n\
            \r   Votos do(a) candidato(a) {nomeGov4}:  {votoGov4}\n\
            \r   Votos do(a) candidato(a) {nomeGov5}:  {votoGov5}\n\
            \r   Votos em branco: {votoGovBranco}\n\
            \r   Votos nulos: {votoGovNulo}\n\
            \r\n * Candidatos a presidente:\n\
            \r   Votos do(a) candidato(a) {nomePres1}:  {votoPres1}\n\
            \r   Votos do(a) candidato(a) {nomePres2}:  {votoPres2}\n\
            \r   Votos do(a) candidato(a) {nomePres3}:  {votoPres3}\n\
            \r   Votos do(a) candidato(a) {nomePres4}:  {votoPres4}\n\
            \r   Votos do(a) candidato(a) {nomePres5}:  {votoPres5}\n\
            \r   Votos em branco: {votoPresBranco}\n\
            \r   Votos nulos: {votoPresNulo}\n\
        ")

    elif op == 4:
        # Finaliza o uso da urna com uma mensagem.
        print('\n[*] Obrigado por utilizar a urna eletrônica!')
        exit()

    # O menu precisa ser repetido para que o usuário
    # possa selecionar mais de uma opção.
    print("\n\n+----------- Urna Eletrônica 2.0 -----------+\n\
        \r|                                           |\n\
        \r| [1] Listar candidatos.                    |\n\
        \r| [2] Iniciar votação.                      |\n\
        \r| [3] Apurar votos.                         |\n\
        \r| [4] Desligar a urna.                      |\n\
        \r|                                           |\n\
        \r+-------------------------------------------+\n\
        \r|\
    ")

    # Variável reposável por armazenar
    # a opção escolhida pelo usuário.
    op = int(input("+--> Digite a sua opção: "))

else:
    # Indica a invalidez da entrada e finaliza
    # a urna com uma mensagem.
    print("\n[!] Opção inválida.")
    print('[*] Obrigado por utilizar a urna eletrônica!')
