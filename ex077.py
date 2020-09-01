'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''
palavras = ('gratis','programar','linguagem','python','curso', 'aprender','estudar','praticar','trabalhar','mercado',
            'programador','futuro')

vogais = ('a','e','i','o','u')

for p in palavras:
    print(f'Na palavra "{p.upper()}" temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in vogais:
            print(f'"{letra}"', end=' ')
    print(' ')

