'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que encontram no
intervalo de 1 até 500.'''
soma = cont = 0
for i in range(1,500,2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')