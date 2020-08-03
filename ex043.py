'''Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
= abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- acima de 40: Obesidade mórbida'''

peso = float(input('Informe o peso (Kg): '))
alt = float(input('Informe a altura (cm): '))/100

imc = peso / (alt**2)

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print(f'Ela está \033[33mabaixo do peso\033[0m.')
elif 18.5 < imc <= 25:
    print(f'Ela está com o peso ideal!')
elif 25 < imc <= 30:
    print(f'Ela está com \033[33msobrepeso\033[0m.')
elif 30 < imc <= 40:
    print(f'Ela está com \033[31mobesidade\033[0m.')
else:
    print(f'Ela está com \033[41mobesidade mórbida\033[0m!')