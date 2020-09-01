'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi maior e o menor
valor digitado e as suas respectivas posições na lista.'''
lista = []
for pos in range(0,5):
    pos = lista.append(int(input(f'Informe um número para a posição {pos}: ')))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi: {max(lista)} e aparece nas posições: ',end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}',end=' ')

print(f'\nO menor valor foi: {min(lista)} e aparece nas posições: ',end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}',end=' ')