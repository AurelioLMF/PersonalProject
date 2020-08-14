'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem masi de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos'''

above18 = mens = girls = 0

while True:
    print('-'*25)
    print(f'Cadastro de pessoas'.center(25))
    print('-'*25)
    idade = int(input('Idade: '))
    sex = ' '
    if idade >= 18:
        above18 += 1

    while sex not in 'MF':
        sex = str(input('Sexo [M ou F]: ')).strip().upper()[0]
        if sex == 'M':
            mens += 1
        elif sex == 'F' and idade <= 20:
            girls += 1

    opt = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opt == 'N':
        break
    print(' ')

print(f'Total de pessoas com mais de 18 anos: {above18}')
print(f'Ao todo temos {mens} homens cadastrados')
print(f'E temos {girls} mulheres com menos de 20 anos')