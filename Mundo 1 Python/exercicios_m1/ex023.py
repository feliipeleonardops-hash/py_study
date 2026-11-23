
# TODO: Desafio 023 - Separando dígitos de um número: Criar um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados (unidade, dezena, centena e milhar)

#! 🧮 Cálculos Matemáticos
# unidade = num // 1 % 10
# dezena  = num // 10 % 10
# centena = num // 100 % 10
# milhar  = num // 1000 % 10

# FORMA MATEMÁTICA
print('VEJA A UNIDADE, DEZENA, CENTENA E MILHAR DO VALOR DIGITADO!')
num = int(input('Digite um valor: '))
unidade = num // 1 % 10
dezena  = num // 10 % 10
centena = num // 100 % 10
milhar  = num // 1000 % 10
print(f'''
O valor digitado foi o de {num}!
Unidade = {unidade}
Dezena = {dezena}
Centena = {centena}
Milhar = {milhar}
''')

# # FORMA STRING
# num = int(input('Informe um número: '))
# n = str(num)
# print(f'Analisando seu número {num}')
# print(f'Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')
# #! Contém erro!    ^