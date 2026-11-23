'''
Desafio 059: Crie um programa que leia DOIS VALORES e mostre um MENU na tela. Seu programa deverá realizar a operação solicitada em cada caso.

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''
print('DIGITE DOIS NÚMEROS E VEJA AS OPÇÕES!')
num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))

option = int(input("""
Escolha as opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Escolha um número: """))

while option == 4:
    print('DIGITE DOIS NÚMEROS E VEJA AS OPÇÕES!')
    num1 = int(input('Primeiro Número: '))
    num2 = int(input('Segundo Número: '))

    option = int(input("""
Escolha as opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Escolha um número: """))
if option == 1:
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')
elif option == 2:
    multiplicar = num1 * num2
    print(f'{num1} x {num2} = {multiplicar} ')
elif option == 3:
    if num1 > num2:
        print(f'Entre {num1} e {num2} o número {num1} é o MAIOR!')
    if num2 > num1:
        print(f'Entre {num1} e {num2} o número {num2} é o MAIOR!')
elif option == 5:
    print('Saindo do programa...')
