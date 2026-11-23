"""
Dsafio 067: Faça um prorgrama que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitador for negativo.
"""

while True:  # loop infinito
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
    print("-" * 20)
