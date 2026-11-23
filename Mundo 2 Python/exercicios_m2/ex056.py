"""
Desafio 056 — Analisador completo: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
"""

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
totmulheres20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: '))
    soma_idade += idade

    if sexo == 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == 'Ff' and idade < 20:
        totmulheres20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é {media_idade:.1f} anos.')
if maior_idade_homem > 0:
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
else:
    print('Não há homens no grupo.')
if totmulheres20 > 0:
    print(f'Existem {totmulheres20} mulheres com menos de 20 anos no grupo.')
