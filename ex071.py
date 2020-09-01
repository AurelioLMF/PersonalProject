'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere que o caixa possui cédulas de 50, 20, 10 e 1'''

print('='*25)
print(f'Banco Catatú'.center(25))
print('='*25)

notas50 = notas20 = notas10 = notas1 = 0
saldo = int(input('Informe o valor a ser sacado: R$ '))

while True:
    while saldo >= 50:
        notas50 = saldo // 50
        saldo %= 50
    if notas50 > 0:
        print(f'Total de cédulas de R$50.00: {notas50}')
    while saldo >= 20:
        notas20 = saldo // 20
        saldo %= 20
    if notas20 > 0:
        print(f'Total de cédulas de R$20.00: {notas20}')
    while saldo >= 10:
        notas10 = saldo // 10
        saldo %= 10
    if notas10 > 0:
        print(f'Total de cédulas de R$10.00: {notas10}')
    while saldo >= 1:
        notas1 = saldo // 1
        saldo %= 1
    if notas1 > 0:
       print(f'Total de cédulas de R$1.00 : {notas1}')
    break
print(' ')
print('Volte sempre! Tenha um bom dia!')