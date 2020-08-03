'''Escreva um programa que faça o computador "pensar" em um númeor inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
pc = randint(0,5)
print('=*='*16)
print(f'\033[33mJogo da Adivinhação!\033[0m'.center(57))
print('''O computador gerou um número inteiro entre 0 e 5.
Tente adivinhar...''')
print('=*='*16)
usuario = int(input('Sua resposta: '))
if usuario == pc:
    print('Você acertou! Conseguiu me vencer...')
else:
    print(f'Você perdeu... O computador gerou o número {pc} e não no {usuario} ')