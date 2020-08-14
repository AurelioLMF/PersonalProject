'''Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} * {i:2} = {n*i}')
    print('')
print('Programa de tabuada encerrado.')