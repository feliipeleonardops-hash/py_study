"""
Listas em Python
"""

# .extend()  # Extende uma lista unindo elementos especificados.
# .append()  # Insere um elemento ao final de uma lista.
# .insert()  # Insere um elemento no lugar que eu quiser de uma lista.
# .pop()     # Remove o último elemento da lista.
# del()      # Remove qualquer elemento da lista.
# clear()    #
# min()      # Pega o menor valor dentro da lista.
# max()      # Pega o maior valor dentro da lista.
# range()    # Não retorna lista
# Função built-in list --> Converte objetos iteráveis (manipular elementos dentro dele) em uma lista.

# Exemplo de lista
# Índice --> utilizado para acessar os valores dentro de uma lista.
#           0    1    2    3    4    5
# lista = ["A", "B", "C", "D", "E", 10.5]
#          -6   -5   -4   -3   -2   -1

#     0  1  2  3  4  5  6  7  8
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


secreto = "perfume"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("Você perdeu!!!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ahh isso não vale! Digite apenas uma letra.")
        continue

    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:
        print(f"WOOW! A letra {letra} existe na palavra secreta.")
    else:
        print(f"AFF! A letra {letra} NÃO EXISTE na palavra secreta.")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"PARABÉNS! Você ganhou!!! A palavra era {secreto_temporario}")
        break
    else:
        print(f"A palavra secretas está assim: {secreto_temporario}")

    if letra not in secreto:
        chances -= 1

    print(f" Você ainda tem {chances} chances.")
print()
