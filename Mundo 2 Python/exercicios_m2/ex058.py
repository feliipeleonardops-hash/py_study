''' Desafio 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forma necessários para vencer'''


from random import randint

print('Vou pensar em um número de 0 a 10. Tente adivinhar ...')
pc = randint(0, 10)
user = int(input('Tente adivinhar digitando um valor entre 0 e 10: '))
while user != pc:
    print('VOCÊ PERDEU! Tenten novamente...')
    user = int(input('Tente adivinhar digitando um valor entre 0 e 10: '))
    if user == pc:
        print('PARABÉNS VOCÊ GANHOU!')
print('Fim do programa!')
