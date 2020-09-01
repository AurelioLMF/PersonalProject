'''Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços. na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Lápis',1.75,
            'Borracha', 2,
            'Caderno',15.90,
            'Estojo', 5,
            'Transferidor', 4.20,
            'Compasso', 10,
            'Mochila', 120,
            'Canetas', 22.30,
            'Livro', 34.90)
print('*='*18)
print(f'{"Listagem de Preços":^36}')
print('=*'*18)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<25}',end='')
    else:
        print(f' R$ {listagem[pos]:>6.2f}')
