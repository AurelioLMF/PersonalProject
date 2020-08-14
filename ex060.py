'''Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5*4*3*2*1 = 120'''

from time import sleep
num = n = int(input('Digite um número para calcular um fatorial: '))
fat = 1

while num > 0:
    fat *= num
    print(f'{num}', end='')
    sleep(0.5)
    print(' * ' if num > 1 else ' = ', end='')
    num -= 1
print(f'{fat}')