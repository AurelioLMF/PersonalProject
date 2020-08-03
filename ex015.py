'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.'''
dias = int(input('Informe quantos dias o carro foi alugado: '))
km = float(input('Informe a quantidade de km rodados: '))

total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R$ {total:.2f}')