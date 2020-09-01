'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número
já existe lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.'''

valores = []

while True:
    num = int(input(f'Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print(f'Número adicionado com sucesso.')
    else:
        print(f'Número duplicado... Não irei adicionar.')
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
print(f'Você digitou os {valores}.')