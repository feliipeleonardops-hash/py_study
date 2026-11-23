"""Desafio 042 — Analisando Triângulos v2.0: Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero (todos os lados iguais), Isósceles (dois lados iguais e um diferente) ou Escaleno (todos os lados diferentes)."""

# Lê os três comprimentos dos segmentos
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# Verifica se os segmentos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")

    # Classifica o tipo de triângulo
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")
