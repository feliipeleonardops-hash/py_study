
# TODO: Desafio 027 - Primeiro e último nome de uma pessoa: Criar um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.

# receber o nome e dividi-lo em partes
n = str(input('Digite seu nome completo: ')).strip()
# Var Divisão
nome = n.split()
# Primeiro nome
print(f'Seu primeiro nome é {nome[0]}')
# Último nome
print(f'Seu último nome é {nome[len(nome)-1]}')
