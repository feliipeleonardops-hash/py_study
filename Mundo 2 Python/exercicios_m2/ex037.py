"""
Desafio 037 — Conversor de Bases Numéricas: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""

# 1. Lê o número inteiro do usuário
num = int(input("Digite um número inteiro: "))

# 2. Mostra o menu de opções
print("""Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL""")

# 3. Lê a escolha do usuário
opcao = int(input("Sua opção: "))

# 4. Faz a conversão usando as funções embutidas do Python
if opcao == 1:
    # bin() retorna o número com '0b' no começo. O [2:] serve para remover isso.
    print(f"O número {num} em BINÁRIO é {bin(num)[2:]}")
elif opcao == 2:
    # oct() retorna com '0o' no começo.
    print(f"O número {num} em OCTAL é {oct(num)[2:]}")
elif opcao == 3:
    # hex() retorna com '0x' no começo.
    print(f"O número {num} em HEXADECIMAL é {hex(num)[2:]}")
else:
    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
