
# TODO: Desafio 010 - Conversor de Moedas: Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Valor atual do Dollar: R$ 5,22

print('CONVERSOR DE MOEDAS')
din = float(input('Digite o valor: '))
dollar = din / 5.22
print(f'Com o valor de R${din}, você poderá obter ${dollar:2f}.')
