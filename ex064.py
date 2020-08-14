'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
(desconsiderando o flag).'''

soma = n = i = 0
while n != 999:
    soma += n
    i += 1
    n = int(input('Digite um número [999 para sair]: '))


print(f'Você digitou {i-1} números e a soma entre eles foi {soma}.')