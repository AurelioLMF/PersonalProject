#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Informe o salário do funcionário: R$ '))
novo_sal = sal *1.15

print(f'O funcionário que ganhava R$ {sal}, com 15% de aumento, passa a receber R$ {novo_sal:.2f}')