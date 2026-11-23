"""
TREINAMENTO PYTHON
"""

valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário: R$ "))
anos_pag = int(input("Pagar em quantos anos: "))
prestacao = valor_casa / (anos_pag * 12)
minimo = salario * 0.30

if prestacao <= minimo:
    print('Empréstimo APROVADOR!')
else:
    print("Empréstimo RECUSADO!")
