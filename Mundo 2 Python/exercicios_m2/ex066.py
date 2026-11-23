"""
Desafio 066: Crie um prorgrama que leia vários números inteiros pelo teclado. O programa só vai para quand o usuário digitar 99, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre ele (desconsiderando o flag).
"""

cont = soma = 0
while cont <= 999:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"Você digitou {cont} números. A soma entre eles vale: {soma}.")
