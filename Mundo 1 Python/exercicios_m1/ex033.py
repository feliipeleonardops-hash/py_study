#
# TODO: Desafio 033 - Maior e menor valores: Criar um programa que leia três números e mostre qual deles é o maior e qual é o menor.

print("DIGITE TRÊS NÚMEROS PARA VER QUAL É O MAIOR E O MENOR!")
n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))
n3 = int(input("Terceiro Número? "))

if n1 > n2 and n1 > n3:
    print(f"O valor {n1} é o maior entre {n2} e {n3}")
elif n2 > n1 and n2 > n3:
    print(f"O valor {n2} é o maior entre {n1} e {n3}")
elif n3 > n1 and n3 > n2:
    print(f"O valor {n3} é o maior entre {n1} e {n2}")
else:
    print("O números digitados contém o mesmo valor!")
print("--FIM--")
