"""
Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma cas. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

print("CÁLCULANDO EMPRÉSTIMO")

# Entrada de dados
val_casa = float(input("Digite o valor da casa R$: "))
sal_comp = float(input("Digite o valor do salário R$: "))
anos = int(input("Quantidade de anos para quitar a casa? "))

# 1. Calcula a prestação REAL da casa (valor total / meses)
prestacao = val_casa / (anos * 12)

# 2. Calcula o LIMITE MÁXIMO permitido (30% do salário)
limite = sal_comp * 0.30

# 3. Compara se a prestação REAL é maior que o limite permitido
if prestacao > limite:
    print(
        f"Valor da prestação mensal é de R${prestacao:.2f} e excede os "
        f"30% permitidos (R${limite:.2f}). \033[1;41mEMPRÉSTIMO NEGADO!\033[m"
    )
else:
    print(
        f"O valor da prestação mensal é de R${prestacao:.2f} e está "
        f"dentro do limite permitido. \033[1;42mEMPRÉSTIMO APROVADO!\033[m"
    )
