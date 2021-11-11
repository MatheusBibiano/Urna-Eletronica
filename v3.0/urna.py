# -*- coding: utf-8 -*-
# Desenvolvido por: Matheus Bibiano & Matheus Cereda

nomePres1 = "Jimi Hendrix"
nomePres2 = "B. B. King"
nomePres3 = "Chuck Berry"
nomePres4 = "Eddie Van Halen"
nomePres5 = "Pete Townshend"

nomeGov1 = "David Gilmour"
nomeGov2 = "Angus Young"
nomeGov3 = "Tony Iommi"
nomeGov4 = "Brian May"
nomeGov5 = "Johnny Ramone"

votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0

votoGov1 = 0
votoGov2 = 0
votoGov3 = 0
votoGov4 = 0
votoGov5 = 0

votoPresNulo = 0
votoPresBranco = 0
votoGovNulo = 0
votoGovBranco = 0

gov = 'GOVERNADOR'
pres = 'PRESIDENTE'

def listarCandidatos():

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


def menuVotacao(govORpres):
    
    print(f"\n\
        \r+------------------------+\n\
        \r|       {govORpres}       |\n\
        \r|                        |\n\
        \r| [1] Votar em candidato.|\n\
        \r| [2] Votar em branco.   |\n\
        \r| [3] Anular voto.       |\n\
        \r|                        |\n\
        \r+------------------------+\n\
        \r|\
    ")


def votarGovPress(nomeCand, votoCand):
    confirmar = input(f'\n>>> Confirmar o voto no candidato {nomeCand}? (s ou n) ')

    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input(f'\n[!] Opção Inválida\n\n>>> Confirmar o voto no candidato {nomeCand}? (s ou n) ')
    if confirmar == 's':
        votoCand += 1
        print('\n[*] Voto Confirmado!')
        return votoCand
    else:
        confirmar == 'n'
        print('\n[!] Voto Cancelado! ')

def votoBranco(branco):
    confirmar = input('\n>>> Confirmar voto em branco? (s ou n) ')
        
    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input('\n[!] Opção Inválida\n\n>>> Confirmar voto em branco? (s ou n) ')
    if confirmar == 's':
        branco += 1
        print('\n[*] Voto em branco Confirmado!')
        return branco
    elif confirmar == 'n':
        print('\n[!] Voto Cancelado')

def anularVoto(nulo):
    confirmar = input('\n>>> Anular voto? (s ou n) ')
        
    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input('\n[!] Opção Inválida\n\n>>> Anular voto? (s ou n) ')
    if confirmar == 's':
        nulo += 1
        print('\n[*] Voto Anulado!')
        return nulo
    elif confirmar == 'n':
        print('\n[!] Voto Cancelado')

def apurarVotos():

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


def desligar():

    print('\n[*] Obrigado por utilizar a urna eletrônica!')
    exit()


def menuUrna():

    print("\n\n+----------- Urna Eletrônica 3.0 -----------+\n\
        \r|                                           |\n\
        \r| [1] Listar candidatos.                    |\n\
        \r| [2] Iniciar votação.                      |\n\
        \r| [3] Apurar votos.                         |\n\
        \r| [4] Desligar a urna.                      |\n\
        \r|                                           |\n\
        \r+-------------------------------------------+\n\
        \r|\
    ")

menuUrna()

op = int(input("+--> Digite a sua opção: "))

while 0 < op <= 4:
    if op == 1:
        listarCandidatos()

    elif op == 2:
        menuVotacao(gov)

        opVoto = int(input('+--> Digite a sua opção: '))

        while (opVoto < 1) or (opVoto > 3):
            print('\n[!] Opção Inválida')
            menuVotacao(gov)
            opVoto = int(input('+--> Digite a sua opção: '))

        if opVoto == 1:
            opCand = int(input('\n>>> Digite o número de seu canditado à governador: '))
            while (opCand < 1) or (opCand > 5):
                opCand = int(input('\n[!] Opção Inválida\n\n>>> Digite o número de seu canditado à governador: '))
            if opCand == 1:
                votoGov1 = votarGovPress(nomeGov1, votoGov1)
            elif opCand == 2:
                votoGov2 = votarGovPress(nomeGov2, votoGov2)
            elif opCand == 3:
                votoGov3 = votarGovPress(nomeGov3, votoGov3)
            elif opCand == 4:
                votoGov4 = votarGovPress(nomeGov4, votoGov4)
            elif opCand == 5:
                votoGov5 = votarGovPress(nomeGov5, votoGov5)

        elif opVoto == 2:
            votoGovBranco = votoBranco(votoGovBranco)

        elif opVoto == 3:
            votoGovNulo = anularVoto(votoGovNulo)

        #SEPARAR

        menuVotacao(pres)

        opVoto = int(input('+--> Digite a sua opção: '))

        while (opVoto < 1) or (opVoto > 3):
            print('\n[!] Opção Inválida')
            menuVotacao(pres)
            opVoto = int(input('+--> Digite a sua opção: '))

        if opVoto == 1:
            opCand = int(input('\n>>> Digite o número de seu canditado à presidente: '))
            while (opCand < 1) or (opCand > 5):
                opCand = int(input('\n[!] Opção Inválida\n\n>>> Digite o número de seu canditado à presidente: '))
            if opCand == 1:
                votoPres1 = votarGovPress(nomePres1, votoPres1)
            elif opCand == 2:
                votoPres2 = votarGovPress(nomePres2, votoPres2)
            elif opCand == 3:
                votoPres3 = votarGovPress(nomePres3, votoPres3)
            elif opCand == 4:
                votoPres4 = votarGovPress(nomePres4, votoPres4)
            elif opCand == 5:
                votoPres5 = votarGovPress(nomePres5, votoPres5)

        elif opVoto == 2:
            votoPresBranco = votoBranco(votoPresBranco)

        elif opVoto == 3:
            votoPresNulo = anularVoto(votoPresNulo)
            
    elif op == 3:
        apurarVotos()

    elif op == 4:
        desligar()

    menuUrna()

    op = int(input("+--> Digite a sua opção: "))

else:

    print("\n[!] Opção inválida.")
    print('[*] Obrigado por utilizar a urna eletrônica!')