'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''

termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = termo + 10*r
cont = 1

while cont <= 10:
    print(f'{termo}',end=' - ')
    termo += r
    cont += 1
print('FIM')