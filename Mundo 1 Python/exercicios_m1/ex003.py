# TODO: Desafio 003 - Somando dois números: Criar um programa que leia dois números inteiros e mostre a soma entre eles.

print("DIGITE DOIS VALORES E VEJA A SOMA ENTRE ELES")
num1 = int(input("Primeiro Valor: "))
num2 = int(input("Segundo Valor: "))
soma = num1 + num2

# FORMA 1 - Com variável...
print("A soma entre {} e {} é de {}".format(num1, num2, soma))  # noqa: UP032

# FORMA 2 - Sem variável de soma
print("A soma entre os valores {} e {} é igual a {}".format(num1, num2, (num1 + num2)))  # noqa: UP032
