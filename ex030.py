#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Informe um número qualquer: '))
if num%2 == 0:
    print(f'O número {num} é \033[035mPAR\033[0m')
else:
    print(f'O número {num} é \033[036mÍMPAR\033[0m')