# -*- coding: utf-8 -*-
# Desenvolvido por: Matheus Bibiano & Matheus Cereda

from variaveis import *
from menus import menuUrna
from listar import listarCandidatos
from votar import iniciarVotacao
from apurar import apurarVotos
from desligar import desligarUrna

# Menu principal da urna.
menuUrna()

# Variável reposável por armazenar
# a opção escolhida pelo usuário.
op = int(input(">>> Digite a sua opção: "))

while True:
    if op == 1:
        listarCandidatos(governadores, presidentes)

    elif op == 2:
        print("\n\t  Votação para governador")
        tipoVoto, valor = iniciarVotacao(governadores, votoGovBranco, votoGovNulo)
        
        if tipoVoto == "confirma":
            for gov in governadores:
                if valor == gov["num"]:
                    gov["qtdVotos"] += 1 # Computando voto ao governador.

        elif tipoVoto == "branco":
            votoGovBranco = valor # Computando voto branco em governador.

        elif tipoVoto == "nulo":
            votoGovNulo = valor # Computando voto nulo em governador.

        print("\n\t  Votação para presidende")
        tipoVoto, valor = iniciarVotacao(presidentes, votoPresBranco, votoPresNulo)
        
        if tipoVoto == "confirma":
            for pres in presidentes:
                if valor == pres["num"]:
                    pres["qtdVotos"] += 1 # Computando voto ao presidente.

        elif tipoVoto == "branco":
            votoPresBranco = valor # Computando voto branco em presidente.

        elif tipoVoto == "nulo":
            votoPresNulo = valor # Computando voto nulo em presidente.
    
    elif op == 3:
        apurarVotos(governadores,
                    presidentes,
                    votoGovBranco,
                    votoPresBranco,
                    votoGovNulo,
                    votoPresNulo)

    elif op == 4:
        desligarUrna()

    else:
        # Indica a invalidez da entrada e finaliza
        # a urna com uma mensagem.
        print("\n[!] Opção inválida.")

    # O menu precisa ser repetido para que o usuário
    # possa selecionar mais de uma opção.
    menuUrna()

    # Variável reposável por armazenar
    # a opção escolhida pelo usuário.
    op = int(input(">>> Digite a sua opção: "))
