'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
base = int(input('Sua opção: '))

if base == 1:
    print(f'O número {num} na base binária = {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} na base octal = {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} na base hexadecimal = {hex(num)[2:]}')
else:
    print('\033[31mOpção inválida!\033[0m')