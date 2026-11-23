
# TODO: Desafio 008 - Conversor de Medidas: Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#!    'km': 1000.0,   # Quilômetro (1.000 metros)
#!    'hm': 100.0,    # Hectômetro (100 metros)
#!    'dam': 10.0,    # Decâmetro (10 metros)
#!    'm': 1.0,       # Metro (Unidade base)
#!    'dm': 0.1,      # Decímetro (0,1 metros)
#!    'cm': 0.01,     # Centímetro (0,01 metros)
#!    'mm': 0.001     # Milímetro (0,001 metros)

print(' CONVERTENDO Metros em cc e MM ')
m = float(input('Digite um metragem: '))
cm = m * (100**2)
mm = m * (1000**2)
print(f'O valor {m}m2 convertido em centímetros {cm}cm, convertido em milímetros {mm}mm')
