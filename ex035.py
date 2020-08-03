#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('=*='*10)
print('Análisador de triângulos'.center(30))
print('=*='*10)

r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('\nOs segmentos acima podem formar um triângulo.')
else:
    print('\nOs segmentos acima \033[31mNÃO\033[0m podem formar um triângulo.')