"""
Desafio 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão usando a estrutura while.
"""

# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa as variáveis de controle
termo_atual = primeiro_termo
contador = 1

print("Os 10 primeiros termos da PA são: ", end="")

# Laço que executa exatamente 10 vezes
while contador <= 10:
    # Exibe o termo atual
    print(f"{termo_atual}", end="")
    # Adiciona uma seta entre os números ou um ponto final no último
    print(" → " if contador < 10 else ".\n", end="")

    # Calcula o próximo termo somando a razão
    termo_atual += razao
    # Incrementa o contador para não criar um laço infinito
    contador += 1
