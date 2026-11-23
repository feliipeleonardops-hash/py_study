# ==================================================================== #! Desafio 028 - Jogo da Adivinhação v.1.0: Criar um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido, mostrando se venceu ou perdeu.

from random import randint

pc = randint(0, 5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
user = int(input("Em que número pensei? "))
if user == pc:
    print("GANHOU!")
else:
    print("PERDEU!")
