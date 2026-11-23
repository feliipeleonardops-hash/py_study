#
# TODO: Desafio 035 - Analisando Triângulo v1.0: Desenvolver um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("Veja se os valores da retas formam um triângulo!")
r1 = float(input("Primeira resta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"As restas {r1}, {r2} e {r3} podem formar um triângulo.")
else:
    print(f"As restas {r1}, {r2} e {r3} NÃO podem formar um triângulo.")
