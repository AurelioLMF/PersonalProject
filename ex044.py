'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição de
pagamento:
- à vista (Dinheiro ou Cheque): 10% de desconto
- à vista (Cartão): 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

nome = ' LOJAS MEXICANAS'
print(f'{nome:*^40}')

valor = float(input('Informe o valor do produto: '))
print('''Formas de pagamento:
[ 1 ] à vista (Dinheiro ou Cheque)
[ 2 ] à vista (Cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    valor_final = 0.9 * valor
elif escolha == 2:
    valor_final = 0.95 * valor
elif escolha == 3:
    valor_final = valor
elif escolha == 4:
    valor_final = 1.2 * valor
    parcelas = int(input('Informe o número de parcelas: '))
    valor_parcelas = valor_final/parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {valor_parcelas:.2f} com juros.')
else:
    valor_final = valor
    print(f'Opção inválida. Tente novamente.')
    print(f'Sua compra de {valor} vai custa{valor_final}.')
print(f'Sua compra de R$ {valor:.2f}, vai custar R$ {valor_final:.2f}.')