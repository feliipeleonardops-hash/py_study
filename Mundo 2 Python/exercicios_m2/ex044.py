#
# Desafio 044 — Gerenciador de Pagamentos: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque (10% de desconto), à vista no cartão (5% de desconto), em até 2x no cartão (preço formal), 3x ou mais no cartão (20% de juros).

# Lê o preço normal do produto
preco = float(input("Preço das compras: R$ "))

# Exibe o menu de opções de pagamento
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque (10% de desconto)
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)""")

# Lê a opção do usuário
opcao = int(input("Qual é a opção? "))

# Processa de acordo com a escolha
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(
        f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final (com 10% de desconto)."
    )
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(
        f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final (com 5% de desconto)."
    )
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será dividida em 2x de R$ {parcela:.2f} sem juros.")
    print(f"O valor total da compra é R$ {total:.2f}.")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} com juros.")
    print(f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.")
else:
    print("Opção inválida de pagamento. Tente novamente!")
