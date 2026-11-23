"""Desafio 052 — Números primos: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num & c == 0:
        print("\033[31m", end=" ")
        tot += 1
    else:
        print("\033[32m", end=" ")
    print(f"{c}", end=" \n")
print(f"O número {num} foi divisível {tot} vezes.")
