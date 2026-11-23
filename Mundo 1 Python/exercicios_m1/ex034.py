#
# TODO: Desafio 034 - Aumentos múltiplos: Criar um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento (10% para salários superiores a R$ 1.250,00 e 15% para inferiores ou iguais).

salario = float(input("Digite o valor do salário: "))
if salario == 1250:
    aumento_10 = salario + (salario * (10 / 100))
    print(
        f"""
        O valor do seu salário é de R${salario} e você receberá um aumento de 10%. Por isso passará a receber R${aumento_10}"""
    )
elif salario < 1250:
    aumento_15 = salario + (salario * (15 / 100))
    print(
        f"""O valor do seu salário é de R${salario} e você receberá um aumento de 15%. Por isso passará a receber R${aumento_15}"""
    )
print("--FIM--")
