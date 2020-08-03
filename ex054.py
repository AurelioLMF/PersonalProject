'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade (21 anos) e quantas já são maiores.'''

from datetime import date
ano_atual = date.today().year
cont_maior = cont_menor = 0

for i in range(1,8):
    ano_nasc = int(input(f'Informe o ano em que a {i}ª pessoa nasceu: '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'\nAo todo tivemos {cont_maior} pessoas maiores de idade.')
print(f'E também tivemos {cont_menor} pessoas menores de idade.')