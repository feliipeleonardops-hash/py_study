
# TODO: Desafio 022 - Analisador de Textos: Criar um programa que leia o nome completo de uma pessoa e mostre:
#! -> O nome com todas as letras em maiúsculas
#! -> O nome com todas as letras em minúsculas
#! -> Quantas letras ao todo (sem espaços)
#! -> Quantas letras tem o primeiro nome.


# ---> Receber o nome completo
nome = str(input('Digite o seu nome completo: ')).strip()
# ---> O nome com todas as letras em maiúsculas
print(f'Seu nome todo em letras maiúsculas fica assim -> {nome.upper()}')

#  ---> O nome com todas as letras em minúsculas
print(f'Seu nome todo em letras minúsculas fica assim -> {nome.lower()}')

# ---> Quantas letras ao todo (sem espaços)
print(f'A quantidade do seu nome sem espaços é de -> {len(nome) - nome.count(' ')} caracteres')

# ---> Quantas letras tem o primeiro nome.
dividir_nome = nome.split()
print(f'A quantidade de letras do seu primeiro nome é de -> {len(dividir_nome[0])} caracteres.')
# print(f'Sei nome tem ao todo {nome.find(' ')}')
