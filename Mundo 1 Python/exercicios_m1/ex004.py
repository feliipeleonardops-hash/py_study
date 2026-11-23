# TODO: Desafio 004 - Dissecando uma Variável: Criar um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele (se é numérico, alfabético, maiúsculo, etc.).

coisa = input("Digite qualquer coisa: ")
print(f"O tipo primitivo é {type(coisa)}")
print("É alfanumérico? ", coisa.isalnum())
print("É alfabético? ", coisa.isalpha())
print("Está todo em maiúsculas? ", coisa.isupper())
print("Está todo em minúsculas? ", coisa.islower())
print("É numérico? ", coisa.isnumeric())
print("Contém espaços? ", coisa.isspace())
print("Está no formato de título?", coisa.istitle())
