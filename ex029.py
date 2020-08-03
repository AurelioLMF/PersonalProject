'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/hm mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 para cada km acima do limite.'''

vel = int(input('Velocidade do carro [km/h]: '))
if vel > 80:
    print(f'\033[31mMultado!\033[0m')
    print(f'Você excedeu o limite permitido de \033[032m80Km/h!\033[0m')
    multa = 7*(vel-80)
    print(f'Deve deve pagar uma multa de R$ {multa:.2f}\n')
print(f'Tenha um bom dia! Dirija com segurança!')