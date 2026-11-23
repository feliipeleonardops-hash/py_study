
# TODO: Desafio 012 - Calculando Descontos: Criar um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

#      Inserir o preço
preco = float(input('Digite o valor R$: '))
#      Calcular quanto vale %5 do valor digitado
val = preco * (5 / 100)
#      Calculo para desconto de %5
desc = preco - val
#      Mostrar na tela o valor com desconto de %5
print(f'O valor de R${preco} com desconto de %5 passará a ser de R${desc}')
