
# TODO: Desafio 018 - Seno, Cosseno e Tangente: Criar um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O âgulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
