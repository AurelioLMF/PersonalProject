'''Crie um programa que vai gerar cinco números aleatórios e colocar um uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os números sorteados foram: ',end='')

for i in tupla:
    print(f'{i}',end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')