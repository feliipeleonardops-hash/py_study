# Desafio 038 — Comparando números: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: "O primeiro valor é maior", "O segundo valor é maior" ou "Não existe valor maior, os dois são iguais.

print("ANALISANDO VALORES")
# Entrada de dados
num1 = int(input("Primeiro Valor: "))
num2 = int(input("Segundo Valor: "))
# condições
if num1 > num2:
    print(f"O primeiro valor ({num1}) é maior do que o segundo ({num2}).")
elif num2 > num1:
    print(f"O segundo valor ({num2}) é maior do que o primeiro ({num1})")
else:
    print("Os valores são iguais.")
print("--FIM--")
