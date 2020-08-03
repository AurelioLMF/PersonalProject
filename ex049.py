#Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um lado for
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11):
    print(f'{i:2} * {num} = {i*num}')