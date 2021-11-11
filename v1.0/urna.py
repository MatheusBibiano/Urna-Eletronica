# -*- coding: utf-8 -*-
# Desenvolvido por: Matheus Bibiano & Matheus Cereda

nomePres1 = "CANDIDATO-1"
nomePres2 = "CANDIDATO-2"
nomePres3 = "CANDIDATO-3"
nomePres4 = "CANDIDATO-4"
nomePres5 = "CANDIDATO-5"

votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0

print("\n\n+----------- Urna Eletrônica 1.0 -----------+")
print("|                                           |")
print("| [1] Listar candidatos.                    |")
print("| [2] Votar para presidente.                |")
print("| [3] Apurar votos.                         |")
print("| [4] Desligar a urna.                      |")
print("|                                           |")
print("+-------------------------------------------+")
print("|")
op = int(input("+--> Digite a sua opção: "))

if op == 1:
    print(f"\n\
        \r+------ Lista de candidatos ------+\n\
        \r|                                 |\n\
        \r| Candidato(a) 1: {nomePres1}     |\n\
        \r| Candidato(a) 2: {nomePres2}     |\n\
        \r| Candidato(a) 3: {nomePres3}     |\n\
        \r| Candidato(a) 4: {nomePres4}     |\n\
        \r| Candidato(a) 5: {nomePres5}     |\n\
        \r|                                 |\n\
        \r+---------------------------------+\n\
    ")

elif op == 2:
    votoPres = int(input('\n>>> Informe o número de seu candidato: '))

    if votoPres == 1:
        confirmar = input(f'\n>>> Confirmar voto no candidato {nomePres1} (s ou n): ')

        if confirmar == 's':
            votoPres1 += 1
            print('\n[*] Voto confirmado!')
            print('[*] Obrigado por utilizar a urna eletrônica!')

        elif confirmar == 'n':
            print('\n[!] Voto cancelado.')
            print('[*] Obrigado por utilizar a urna eletrônica!')
        
        else:
            print("\n[!] Opção inválida.")
            print('[*] Obrigado por utilizar a urna eletrônica!')

    elif votoPres == 2:
        confirmar = input(f'\n>>> Confirmar voto no candidato {nomePres2} (s ou n): ')

        if confirmar == 's':
            votoPres2 += 1
            print('\n[*] Voto confirmado!')
            print('[*] Obrigado por utilizar a urna eletrônica!')

        elif confirmar == 'n':
            print('\n[!] Voto cancelado.')
            print('[*] Obrigado por utilizar a urna eletrônica!')
        
        else:
            print("\n[!] Opção inválida.")
            print('[*] Obrigado por utilizar a urna eletrônica!')

    elif votoPres == 3:
        confirmar = input(f'\n>>> Confirmar voto no candidato {nomePres3} (s ou n): ')

        if confirmar == 's':
            votoPres3 += 1
            print('\n[*] Voto confirmado!')
            print('[*] Obrigado por utilizar a urna eletrônica!')

        elif confirmar == 'n':
            print('\n[!] Voto cancelado.')
            print('[*] Obrigado por utilizar a urna eletrônica!')
        
        else:
            print("\n[!] Opção inválida.")
            print('[*] Obrigado por utilizar a urna eletrônica!')

    elif votoPres == 4:
        confirmar = input(f'\n>>> Confirmar voto no candidato {nomePres4} (s ou n): ')

        if confirmar == 's':
            votoPres4 += 1
            print('\n[*] Voto confirmado!')
            print('[*] Obrigado por utilizar a urna eletrônica!')

        elif confirmar == 'n':
            print('\n[!] Voto cancelado.')
            print('[*] Obrigado por utilizar a urna eletrônica!')
        
        else:
            print("\n[!] Opção inválida.")
            print('[*] Obrigado por utilizar a urna eletrônica!')

    elif votoPres == 5:
        confirmar = input(f'\n>>> Confirmar voto no candidato {nomePres5} (s ou n): ')

        if confirmar == 's':
            votoPres5 += 1
            print('\n[*] Voto confirmado!')
            print('[*] Obrigado por utilizar a urna eletrônica!')

        elif confirmar == 'n':
            print('\n[!] Voto cancelado.')
            print('[*] Obrigado por utilizar a urna eletrônica!')
        
        else:
            print("\n[!] Opção inválida.")
            print('[*] Obrigado por utilizar a urna eletrônica!')
      
    else:
        print('\n[!] Opção inválida.')
        print('[*] Obrigado por utilizar a urna eletrônica!')

elif op == 3:
    print(f"\n\
        \r+------------ Apuração de votos --------------+\n\
        \r|                                             |\n\
        \r| Votos do(a) candidato(a) {nomePres1}:  {votoPres1}    |\n\
        \r| Votos do(a) candidato(a) {nomePres2}:  {votoPres2}    |\n\
        \r| Votos do(a) candidato(a) {nomePres3}:  {votoPres3}    |\n\
        \r| Votos do(a) candidato(a) {nomePres4}:  {votoPres4}    |\n\
        \r| Votos do(a) candidato(a) {nomePres5}:  {votoPres5}    |\n\
        \r|                                             |\n\
        \r+---------------------------------------------+\n\
    ")

elif op == 4:
    print('\n[*] Obrigado por utilizar a urna eletrônica!')

else:
    print('\n[!] Opção inválida.')
    print('\n[*] Obrigado por utilizar a urna eletrônica!')