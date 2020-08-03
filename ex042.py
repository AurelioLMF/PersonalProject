'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
print('=*='*10)
print('Análisador de triângulos'.center(30))
print('=*='*10)

r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('\nOs segmentos acima podem formar um triângulo',end='')
    if r1 == r2 == r3:
        print('\033[34mequilátero\33[0m.')
    elif r1 != r2 != r3 != r1:
        print('\033[34mescaleno\033[0m.')
    else:
        print('\033[34misósceles\033[0m.')
else:
    print('\nOs segmentos acima \033[31mNÃO\033[0m podem formar um triângulo.')