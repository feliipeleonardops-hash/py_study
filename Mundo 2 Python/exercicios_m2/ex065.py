"""
Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

# Inicializa as variáveis de controle e cálculo
soma = contador = maior = menor = 0
resposta = "S"

# O laço continua rodando enquanto a resposta for 'S'
while resposta in "SSIM":
    numero = int(input("Digite um número: "))

    soma += numero
    contador += 1

    # Lógica para definir o maior e o menor valor
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    # Pergunta se o usuário deseja continuar e padroniza a resposta em maiúscula
    resposta = str(input("Quer continuar? [S/N]: ")).strip().upper()

# Calcula a média real dos valores lidos
media = soma / contador

# Exibe os resultados na tela
print("-" * 40)
print(f"Você digitou {contador} números e a média foi {media:.2f}")
print(f"O maior valor lido foi {maior} e o menor foi {menor}")
print("-" * 40)
