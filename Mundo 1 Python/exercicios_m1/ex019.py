
# TODO: Desafio 019 - Sorteando um item na lista: Criar um programa que ajude um professor lendo o nome de quatro alunos e sorteando um deles para apagar o quadro.

from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}!')
