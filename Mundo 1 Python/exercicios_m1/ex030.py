#
# TODO: Desafio 030 - Par ou Ímpar?: Criar um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número: "))

# condição
if num % 2 == 0:
    print(f"O número {num} é PAR!")
else:
    print(f"O número {num} é ÍMPAR!")
