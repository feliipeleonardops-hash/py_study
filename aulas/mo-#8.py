# 📌 CONCEITO DE IMPORTAÇÃO
import math  # Importa a biblioteca INTEIRA (exige usar 'math.função')
from math import ceil, sqrt  # Importa apenas funções ESPECÍFICAS (usa a função direto)

"""
# 🧮 BIBLIOTECA 'math' (Principais Funções)
• ceil      -> Arredonda para CIMA
• floor     -> Arredonda para BAIXO
• trunc     -> Elimina a parte decimal (corta a vírgula)
• pow       -> Potência
• sqrt      -> Raiz quadrada
• factorial -> Cálculo fatorial
"""

# ⚡ Exemplo 1: Importando a biblioteca completa
import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f}")
print(f"Arredondado para cima: {math.ceil(raiz)}")


# ⚡ Exemplo 2: Importando apenas o que vai usar
from math import sqrt

num = int(input("Digite um número: "))
raiz = sqrt(num)  # Não precisa usar "math." antes
print(f"A raiz de {num} é igual a {raiz:.2f}")


# 🎲 NÚMEROS ALEATÓRIOS (Biblioteca 'random')
import random

num_aleatorio = random.randint(1, 10)  # Gera um número inteiro entre 1 e 10
print(f"Número gerado: {num_aleatorio}")


# 🎨 BIBLIOTECAS EXTERNAS (Ex: 'emoji')
# Instalação necessária no terminal: pip install emoji
import emoji

print(emoji.emojize("Python é fantástico! 🤷‍♀️ :thumbs_up: :snake:"))
