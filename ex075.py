'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes aparece o número 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares'''

num = (int(input('Informe um número: ')),
        int(input('Informe outro número: ')),
        int(input('Informe mais um número: ')),
        int(input('Informe o último número: ')))

print(f'Você digitou os seguintes valores: {num}')
print(f'O número 9 aparece {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O número 3 não foi digitado em nenhuma posição')
print(f'Os números pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')