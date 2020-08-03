'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50
por Km para viagens de até 200 Km e R$0.45 para viagens mais longas.'''

distancia = float(input('Informe a distância de sua viagem [Km]: '))
if distancia <= 200:
    preco = 0.5 * distancia
else:
    preco = 0.45 * distancia

print(f'Você está prestes a começar uma viagem de {distancia:.1f} Km')
print(f'O valor da passagem é de R${preco:.2f}')