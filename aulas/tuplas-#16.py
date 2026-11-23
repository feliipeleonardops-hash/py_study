# Aula #16 - TUPLAS
"""
Existem TRẼS Tipos de variáveis compostas

1º Tuplas -> () São imutáveis
2º Listas -> []
3º Dicionário -> {}
"""

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
# print(lanche[-1])
# print(len(lanche))
# print(lanche)

# MODO 1 - Sem Posição Localizada
for comida in lanche:
    print(f"Eu vou comer {comida}!")

# MODO 2 - Com Posição Localizada
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("Comi pra caramba!")
print("-" * 27)
# 2.1
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} e nã posição {pos}")
print("Comi pra caramba!")

# sorted -> MOSTRA tuplas em ordem, mas sem alterar.
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # concatenação
print(c.index(8))  # .index -> Revela qual a posição de um elemento
print()

pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)
