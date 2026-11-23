"""
LAÇO DE REPETIÇÃO: FOR e WHILE
"""

"""ESTRUTURA BASE FOR"""
#              i, f, p
for n in range(0, 100, 8):
    print(n)
print("Fim do programa!")

for n in range(100):
    if n % 8 == 0:  # Obter múltiplos
        print(n)
# continue --> Pula para o próximo laço
# break --> Termina o laço

"""ESTRUTURA BASE WHILE"""
contador = 1  # Demilitador
acumulador = 1  # Acumular valores

while contador <= 10:  # ENQUANTO condição for verdadeira, execute
    print(f"{acumulador, contador}")
    acumulador += contador
    contador += 1  # incrementação
print("Fim do programa!")
