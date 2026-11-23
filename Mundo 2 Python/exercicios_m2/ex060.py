"""
Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex.: 5! = 5x4x3x2x1 = 120
"""

# Lê o número fornecido pelo usuário
numero = int(input("Digite um número para calcular seu fatorial: "))

# Inicializa as variáveis
contador = numero
fatorial = 1

print(f"Calculando {numero}! = ", end="")

# Laço de repetição para o cálculo e exibição
while contador > 0:
    print(f"{contador}", end="")
    # Adiciona o 'x' entre os números ou o '=' no final
    print("x" if contador > 1 else " = ", end="")

    fatorial *= contador
    contador -= 1

# Exibe o resultado final
print(f"{fatorial}")
