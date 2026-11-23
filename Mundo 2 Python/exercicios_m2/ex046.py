"""
Desafio 046 — Contagem regressiva: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

import time

print("CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIO")
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print("FELIZ DIA!")
