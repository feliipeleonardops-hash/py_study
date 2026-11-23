"""
Desafio 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada, No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

# Inicializa as variáveis de contagem e soma
contador = 0
soma = 0

# Lê o primeiro número fora do laço
numero = int(input("Digite um número [999 para parar]: "))

# O laço roda enquanto o número digitado não for o flag (999)
while numero != 999:
    soma += numero
    contador += 1

    # Lê o próximo número no final do laço
    numero = int(input("Digite um número [999 para parar]: "))

# Exibe os resultados finais
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")
