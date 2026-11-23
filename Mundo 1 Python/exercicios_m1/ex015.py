
# TODO: Desafio 015 - Aluguel de Carros: Escrever um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado, calculando o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 ṕr Km rodado.

# Receber quantos KM rodados e quantos DIAS alugado.
km = float(input('Quantos Km percorridos: '))
dias = int(input('Quanto dias alugados? '))

# Calculo dos Km
cal_km = km * 0.15
# Calculo dos dias
cal_dias = dias * 60
# Calculo do total a ser pago
total = cal_dias + cal_km

print(f'{km} km rodados, {dias} dias alugado.')
print('Calculando total...')
print(f'O valor total de dias alugado e km rodados foi de R${total}')