"""Desafio 054 — Grupo da Maioridade: Crie um programa que leia o ano de nascimento de sete pessoas
. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""

# 0. Capturar a data atual
from datetime import date

atual = date.today().year  # noqa: DTZ011

# 1. Criar os contadores antes do loop
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input(f"Em que ano a {c}ª pessoa nasceu? "))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"""
Ao todo tivemos {totmaior} pessoas maiores de idade.
E também tivemos {totmenor} pessoas menores de idade.""")
