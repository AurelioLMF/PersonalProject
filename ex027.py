'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
prim = nome[0]
ult = nome[-1]

print(f'Nome completo: {n}\nPrimeiro nome: {prim}\nÚltimo nome: {ult}')