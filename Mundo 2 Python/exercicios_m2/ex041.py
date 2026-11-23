"""Desafio 041 — Classificando Atletas: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: até 9 anos (Mirim), até 14 anos (Infantil), até 19 anos (Júnior), até 25 anos (Sênior), acima de 25 anos (Master)."""

from datetime import datetime

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.now().year  # noqa: DTZ005
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"Você tem {idade} anos e faz parte da categoria MIRIM.")
elif idade <= 14:
    print(f" Você tem {idade} anos e faz parte da categria INFANTIL.")
elif idade <= 19:
    print(f" Você tem {idade} anos e faz parte da categoria JÚNIOR.")
elif idade <= 25:
    print(f" Você tem {idade} anos e faz parte da categoria SÊNIOR.")
else:
    print(f" Você tem {idade} anos e faz parte da categoria MASTER.")
print("FIM")
