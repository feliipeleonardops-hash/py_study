#
# Desafio 045 — GAME: Pedra Papel e Tesoura: Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você.

import time
from random import randint

# Cria a tupla com as opções do jogo
itens = ("Pedra", "Papel", "Tesoura")

# O computador escolhe um número entre 0 e 2
computador = randint(0, 2)

# Exibe o menu para o jogador
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input("Qual é a sua jogada? "))

# Valida se a jogada do usuário é válida
if jogador not in [0, 1, 2]:
    print("JOGADA INVÁLIDA! Tente novamente.")
else:
    # Efeito de suspense (JO - KEN - PÔ)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PÔ!!!")
    print("-=" * 15)

    # Mostra o que cada um escolheu
    print(f"O computador escolheu {itens[computador]}")
    print(f"O jogador escolheu {itens[jogador]}")
    print("-=" * 15)

    # Condições de vitória, derrota ou empate
    if computador == 0:  # Computador jogou PEDRA
        if jogador == 0:
            print("EMPATE!")
        elif jogador == 1:
            print("JOGADOR VENCEU!")
        elif jogador == 2:
            print("COMPUTADOR VENCEU!")

    elif computador == 1:  # Computador jogou PAPEL
        if jogador == 0:
            print("COMPUTADOR VENCEU!")
        elif jogador == 1:
            print("EMPATE!")
        elif jogador == 2:
            print("JOGADOR VENCEU!")

    elif computador == 2:  # Computador jogou TESOURA
        if jogador == 0:
            print("JOGADOR VENCEU!")
        elif jogador == 1:
            print("COMPUTADOR VENCEU!")
        elif jogador == 2:
            print("EMPATE!")
