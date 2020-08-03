#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
cont = 0
for i in range(1,num+1):
    if num % i == 0:
        print(f'\033[33m{i}',end='\033[0m ')
        cont += 1
    else:
        print(f'\033[31m{i}',end='\033[0m ')
print(f'\nO número {num} foi divisível {cont} vezes.')
if cont == 2:
    print(f'E por isso ele é primo')
else:
    print(f'E por isso ele não é primo')