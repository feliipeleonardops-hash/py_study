"""
Desafio 070: Crie um prorgrama que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.
"""

total = totmil = menor = cont = 0
barato = ""

while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$ "))
    cont += 1

    # TOTAL
    total += preço
    if preço > 1000:
        totmil += 1

    # MENOR
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    # PERGUNTA / SAIR DO PROGRAMA
    resp = " "
    while resp not in "SN":
        resp = str(input("Que continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

    print("{:-^40}".format("FIM DO PROGRAMA"))
    print(f"O total da compra foi R$ {total:.2f}")
    print(f"Temos {totmil} produtos custando acima de R$ 1000")
    print(f"O produto mais barato foi {barato} que custa {menor:.2f}")
