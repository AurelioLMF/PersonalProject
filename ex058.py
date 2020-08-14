'''Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

cpu = randint(0,10)
print('''Bem-vindo ao jogo da adivinhação!
O computador pensou em um número, consegue adivinhar qual?''')

palpite = 1
acertou = False

while not acertou:
    jogador = int(input(f'Seu {palpite}º palpite: '))
    if jogador == cpu:
        acertou = True
    elif jogador < cpu:
        print('Mais...')
        palpite += 1
    else:
        print('Menos...')
        palpite += 1
print(f'Parabéns! Você precisou de {palpite} palpite(s)!')