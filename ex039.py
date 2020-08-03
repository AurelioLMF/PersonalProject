'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora de se alistar ou se já passou o tempo do alistamento. Seu programa também deve
mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')
alist = 18
if idade < alist:
    ano_rest = alist - idade
    print(f'Ainda faltam {ano_rest} anos para o seu alistamento.')
    saldo = ano_atual + ano_rest
    print(f'O seu alistamente será em {saldo}.')
elif idade == alist:
    print(f'Está na hora de se alistar \033[33mIMEDIATAMENTE\033[0m!')
elif idade > alist:
    ano_alist = ano_atual - (ano_nasc+18)
    print(f'Você já deveria ter se alistado há {ano_alist} anos atrás.')
    ano_nasc += 18
    print(f'Seu alistamento foi em {ano_nasc}')