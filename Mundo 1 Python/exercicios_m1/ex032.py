#
# TODO: Desafio 032 - Ano Bissexto: Criar um programa que leia um ano qualquer e mostre se ele é bissexto.

print("DIGITE O ANO PARA VER SE ELE É BISSEXTO")
ano = int(input("Digite o ano: "))

# condição
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é BISSEXTO!")
else:
    print("Esse ano não é bissexto.")
