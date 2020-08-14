'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência de Fibonacci.
Ex.: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

n = int(input('Informe quantos termos você quer mostrar: '))
primtermo = 0
segtermo = 1
cont = 3

print(f'{primtermo} - {segtermo}',end = ' - ')
while cont <= n:
 terctermo = segtermo + primtermo
 primtermo = segtermo
 segtermo = terctermo
 cont += 1
 print(f'{terctermo}', end =' - ')
print('FIM')