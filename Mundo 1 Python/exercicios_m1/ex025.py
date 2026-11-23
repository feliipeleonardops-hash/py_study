
# TODO: Desafio 025 - Procurando uma string dentro de outra: Criar um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

# receber o nome e transformar em minúsculas
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem SILVA? {'silva' in nome.lower()}')
