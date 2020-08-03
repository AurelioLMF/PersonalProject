'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor_casa = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos_fin = int(input('Informe o tempo de financiamento em anos: '))

prestacao = valor_casa/(anos_fin*12)

print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_fin} anos, a prestação será de R$ {prestacao:.2f}')

if prestacao <= sal*0.3:
    print(f'Empréstimo concedido!')
else:
    print(f'Empréstimo \033[031mNEGADO\033[0m.')