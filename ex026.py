'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece pela última vez'''

frase = str(input('Digite uma frase: ')).upper().strip()
cont = frase.count('A')

print(f'A letra "A" aparece {cont} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A letra "A" apareceu pela última vez na posição {frase.rfind("A")+1}')

