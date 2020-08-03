'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex.: Apos a sopa
A sacada da casa
A torre da derrota
o lobo ama o bolo
Anotaram a data da maratona'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')