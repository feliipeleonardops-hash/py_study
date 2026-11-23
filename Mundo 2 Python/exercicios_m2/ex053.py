"""Desafio 053 — Detector de Palíndromo: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços"""

frase = str(input("Digite um frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
# inverso = ""
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print("Temo um palíndromo!")
else:
    print("A frase digitada não é um palíndromo.")
