'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$1.00 = R$ 3.27'''

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/5.212
euro = real/6.16
dolar_euro = 5.212/6.16
print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}')
print(f'Com R$ {real:.2f} você pode comprar € {euro:.2f}')
