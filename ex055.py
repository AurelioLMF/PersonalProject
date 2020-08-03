#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos
maior_peso = 0

for i in range(1,6):
    peso: float = float(input(f'Peso da {i}ª pessoa [Kg]: '))
    if i == 1 or peso < menor_peso:
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso

print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')