'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Informe o salário: R$ '))
if sal <= 1250:
    novosal = sal*1.15
else:
    novosal = sal*1.1
print(f'Quem ganhava R$ {sal:.2f} passa a ganhar R$ {novosal:.2f} agora')
