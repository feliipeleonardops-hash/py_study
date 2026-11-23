#
# Desafio 039 — Alistamento Militar: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

print("ALISTAMENTO MILITAR!")
# Entrada de dados
idade = int(input("Digite o ano em que nasceu: "))
ano_atual = datetime.now().year  # noqa: DTZ005
idade_alistar = ano_atual - idade
saldo = 18 - idade_alistar  # Quando tem menos de 18:
ano = ano_atual + saldo
saldo1 = idade_alistar - 18  # Quando tem mais de 18:
ano = ano_atual - saldo
# condições para alistamento militar
# cond.1: se ele ainda vai se alistar ao serviço militar
if idade_alistar < 18:
    print(f"Você tem {idade_alistar} anos. Ainda vai se alistar daqui a {saldo} ano(s)")
elif idade_alistar == 18:
    print(f"Você tem {idade_alistar} anos. Deve se alistar no ano atual.")
elif idade_alistar > 18:
    print(f"Você tem {idade_alistar} anos. Já passou {saldo1} ano(s) do prazo.")
