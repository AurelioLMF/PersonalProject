'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$ 1.000,00
c) Qual o nome do produto mais barato.'''

print('*='*13)
print(f'Lojas MeXiCaNas'.center(26))
print('*='*13)

total = cont = above1t = 0
nome_prod = ' '
while True:
    prod = str(input('Nome do produto: ')).title()
    valor = float(input('Preço: R$ '))
    total += valor
    cont += 1

    if cont == 1:
        menor = valor

    if valor >= 1000:
        above1t += 1

    elif valor < menor:
        menor = valor
        nome_prod = prod

    opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
    print(' ')
print(f'\nO total da compra é de R$ {total:.2f}')
print(f'Temos {above1t} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {nome_prod} que custa R$ {menor}')