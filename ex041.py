'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SENIOR
- acima: MASTER'''

from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: MIRIM')
elif idade <= 14:
    print(f'Classificação: INFANTIL')
elif idade <= 19:
    print(f'Classificação: JUNIOR')
elif idade <= 25:
    print(f'Classificação: SÊNIOR')
else:
    print(f'Classificação: MASTER')