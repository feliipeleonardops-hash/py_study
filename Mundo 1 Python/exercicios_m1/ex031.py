#
# TODO: Desafio 031 - Custo da Viagem: Desenvolver um programa que pergunte a distância de uma viagem em km e calcule o preço da passagem (R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas).

dist = float(input("Qual a distância percorrida? "))


if dist <= 200:
    km = dist * 0.50
    print(
        f"""Você percorreu {dist}km na sua viagem. O valor cobrado pelas viagens de até 200km é de R$0.50 por km. E você pagará o valor de  R${dist + km}"""
    )
elif dist > 200:
    vl = dist * 0.45
    print(
        f"""Você percorreu {dist}km na sua viagem. O valor cobrado pelas viagens acima de 200km é de R$0.45 por km.Você pagará o valor de R${vl}"""
    )
