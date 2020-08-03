#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

lista = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Sua escolha: '))

print('JO')
sleep((0.5))
print('KEN')
sleep((0.5))
print('PÔ')
sleep((0.5))

print('=*=' * 9)
print(f'O computador jogou {lista[pc]}')
print(f'Você jogou {lista[jogador]}')
print('=*=' * 9)

if pc == 0: #computador jogou pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('Jogada inválida')

elif pc == 1: #computador jogou papel
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada inválida')

elif pc == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('Empatou')
    else:
        print('Jogada inválida')

