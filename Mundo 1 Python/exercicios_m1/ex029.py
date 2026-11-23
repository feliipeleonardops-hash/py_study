#
#! Desafio 029 - Radar eletrônico: Criar um programa que leia a velocidade de um carro; se ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado e calcule o valor da multa (R$ 7,00 por km acima do limite).

print("RADAR ELETRÔNICO")
velocidade = float(input("Qual foi a velocidade do carro: "))

if velocidade >= 81:
    multa = (velocidade - 80) * 7
    print(f"""Você ultrapassou o limite de 80 km/h.
    Multa a pagar no valor de R$ {multa:.2f}""")
else:
    print("Dentro do limte permitido!")
