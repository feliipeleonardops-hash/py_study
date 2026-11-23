#
# Desafio 040 — Aquele clássico da Média: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida: Média abaixo de 5.0 (Reprovado), Média entre 5.0 e 6.9 (Recuperação), ou Média 7.0 ou superior (Aprovado)

# Entrada de dados
n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))
media = (n1 + n2) / 2
# condições


if media < 5.0:
    print(f"Sua médio foi de {media} e você está \033[1;41mREPROVADO!\033[m")
elif media > 5.0 and media < 6.9:
    print(f"Sua média foi de {media} e você está de \033[1;43mRECUPERAÇÃO!\033[m")
elif media >= 7.0:
    print(f"Sua média foi de {media} e você foi \033[1;42mAPROVADO!\033[m")
print("--FIM--")
