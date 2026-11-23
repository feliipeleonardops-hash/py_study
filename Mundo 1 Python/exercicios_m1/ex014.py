
# TODO: Desafio 014 - Conversor de Temperaturas: Escrever um programa que converta uma temperatura digitada em graus Celsius (°C) para graus Fahrenheit (°F).

print('CONVERTENDO GRAUS CELSIUS (°C) EM FAHRENHEIT (°F)')

# Receber o valor em Celsius (°C).
celsius = float(input('Digite a temperatura em °C:: '))

# Calculo da conversão
fah = (celsius * 1.8) + 32

# Exibir na tela o resultado
print(f'O valor {celsius:.1f}°C convertido é de {fah:.1f}°F')