'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos'''
soma_idade = media = maior_idade = cont_fem = 0

for i in range(1,5):
    print(f'----- {i}ª Pessoa -----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if idade > maior_idade and sexo in 'M':
        maior_idade = idade
        maior_nome = nome

    if idade < 20 and sexo in 'F':
        cont_fem += 1

    soma_idade += idade

media = soma_idade / 4
print(f'\nA média de de idade do grupo é de: {media}')
print(f'O homem mais velho tem {maior_idade} anos e se chama {maior_nome}.')
print(f'Ao todo são {cont_fem} mulheres com menos de 20 anos.')