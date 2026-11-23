"""
Desafio 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)

# Lê a quantidade de termos desejada
n = int(input("Quantos termos você quer mostrar? "))

# Inicializa os dois primeiros termos da sequência
t1 = 0
t2 = 1

print("~" * 30)

# Trata os primeiros casos e inicia o laço se n for maior que 2
if n <= 0:
    print("Por favor, digite um número maior que 0.")
elif n == 1:
    print(f"{t1} → FIM")
else:
    # Mostra os dois primeiros termos que já estão definidos
    print(f"{t1} → {t2}", end="")

    # O contador começa em 3 porque os 2 primeiros termos já foram impressos
    contador = 3

    while contador <= n:
        # O próximo termo é sempre a soma dos dois anteriores
        t3 = t1 + t2
        print(f" → {t3}", end="")

        # Faz o "revezamento" das variáveis para avançar na sequência
        t1 = t2
        t2 = t3

        contador += 1

    print(" → FIM")
print("~" * 30)
