'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2)/2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')
if media < 5:
    print(f'O aluno está \033[31mREPROVADO\033[0m')
elif 5 <= media < 7:
    print(f'O aluno está de \033[33mRECUPERAÇÃO\033[0m')
else:
    print(f'O aluno está \033[36mAPROVADO\033[0m')