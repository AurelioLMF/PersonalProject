'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vítórias consecutivas que ele conquistou no final do jogo.'''

print('*='*15)
print(f'Jogo do Par ou íMPAR'.center(30))
print('*='*15)
from random import randint
from time import sleep

v = 0
while True:
    cpu = randint(0, 10)
    jog = str(input('Par ou Ímpar [P ou I]: ')).strip().upper()[0]
    num_jog = int(input('Informe seu número - entre 0 e 10: '))
    soma = num_jog + cpu
    sleep(0.5)
    print('Dô',end=', ')
    sleep(0.5)
    print('lá',end=', ')
    sleep(0.5)
    print('si...')
    sleep(0.75)
    print('Já!')
    sleep(0.25)
    print(f'Você jogou {num_jog} e o computador {cpu}. Soma = {soma},',end=' ')
    print('é PAR.' if soma % 2 == 0 else 'é ÍMPAR.')

    if soma % 2 == 0 and jog == 'P':
        print(f'Você venceu!')
        v += 1
    elif soma % 2 != 0 and jog == 'I':
        print(f'Você venceu!')
        v += 1
    else:
        print(f'Fim de jogo! Você perdeu...')
        break
    print('Odeio perder... Vamos jogar novamente!\n')
print(f'Total de vitórias: {v}')