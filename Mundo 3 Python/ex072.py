"""
Desafio 072: Crie um prorgrama que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

cont = (
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Quatorze",
    "Quinze",
    "Desesseis",
    "Desessete",
    "Dezoito",
    "Dezenove",
    "Vinte",
)

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    num = int(input("Tente novamente. Digite um número entre 0 e 20: ", end + ""))
print(f"Você digitou o número {cont[num]}!")
