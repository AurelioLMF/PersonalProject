'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras no total (sem considerar espaços)
- Quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas {nome.upper()}')
print(f'Seu nome em minúsculas {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
primeiro = nome.split()[0]
print(f'Seu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras')