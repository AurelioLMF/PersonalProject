'''Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
quando ele disser que quer mostrar 0 termos.'''

termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = termo + 10*r
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}',end=' - ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão formatada com {total} mostrados.')