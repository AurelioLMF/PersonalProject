'''Crie um programa que leia dois valores e mostre um menu como apresentado abaixo. Seu programa deverá realizar a
operação solicitada em cada caso:
[ 1 ] somar
[ 2 ] multiplicador
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    escolha = int(input('''O que deseja fazer?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Sua escolha: '''))

    if escolha == 1:
        soma = n1+n2
        print(f'A soma entre os valores {n1} e {n2} = {soma}')
    elif escolha == 2:
        mult = n1*n2
        print(f'A multiplicação entre os valores {n1} e {n2} = {mult}')
    elif escolha == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print(f'Entre {n1} e {n2}, o maior é {maior}')
    elif escolha == 4:
        n1 = int(input('Informe os números novamente. \nPrimeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
    print('+=' * 10)
print(f'Fim do programa!')