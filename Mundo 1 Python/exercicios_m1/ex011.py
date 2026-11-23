
# TODO: Desafio 011 - Pintando Parede: Criar um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m².

print('='*30)
print('CALCULANDO O Metro Quadrado')
print('='*30)
alt = float(input('Digite a altura: '))
larg = float(input('Digite a largura: '))
metros = larg * alt
print(f'A área total é de {metros:.1f}')
print('='*30)