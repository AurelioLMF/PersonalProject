'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.'''

opt = 'S'
soma = cont = maior = menor = 0
while opt == 'S':
    n = int(input('Digite um número: '))
    opt = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

media = soma/cont
print(f'Você digitou {cont} valores e a média foi {media}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')