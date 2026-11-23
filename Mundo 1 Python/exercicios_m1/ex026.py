
# TODO: Desafio 026 - Primeira e última ocorrência de uma string: Criar um programa que leia uma frase pelo teclado e mostre:
#! Quantas vezes aparece a letra "A"
#! Em qual posição ela aparece pela primeira vez
#! Em que posição aparece pela última vez.

# recebe a frase e transforma tudo em minúsculas
frase = str(input('Digite uma frase: ')).lower().strip()
print(f'Quantas vezes aparece a letra A dentro da frase? {frase.count('a')} vezes.')

# Em qual POSIÇÃO ela aparece pela PRIMEIRA VEZ.
print(f'A letra A aparece pela primeira vez na posição {frase.find('a')+1}')

# Em que POSIÇÃO aparece pela ÚLTIMA VEZ.
print(f'A última letra A apareceu na posição {frase.rfind('a')+1}')