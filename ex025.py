#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = str(input('Informe seu nome completo: ')).strip().upper()
print(f'Seu nome tem Silva? {"SILVA" in nome}')