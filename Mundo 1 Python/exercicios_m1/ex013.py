
# TODO: Desafio 013 - Reajuste Salarial: Criar um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.

#       Receber valor do salário
valor_salario = float(input('Digito o valor do salário atual R$: '))

#       Calcular quanto é 15% do valor recebido
cal_1 = valor_salario * (15 / 100)

#       Calculo de aumento (15%)
aumento = valor_salario + cal_1

#       Mostrar na tela
print(f'O valor atual é R${valor_salario} e com 15% de aumento passará a ser de R${aumento}')
