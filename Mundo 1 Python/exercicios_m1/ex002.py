# TODO: Desafio 002 - Respondendo ao Usuário**: Criar um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# FORMA 1 - Simples com variável
nomee = str(input("Digite seu nome: "))
print("É um prazer te conhecer", nomee)

# FORMA 2 # ! --- .format() ---
nomeee = str(input("Digite seu nome: "))
print("É um prazer te conhecer, {}!".format(nomeee))  # noqa: UP032

# FORMA 3 - # ! --- f' {mask} - {mask}' ---
nome = str(input("Digite seu nome: "))
print(f"Olá, {nome}! É um prazer te conhecer!")
