'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

ext = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
       'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('\033[31mNúmero inválido. Tente novamente.\033[0m')
    else:
        print(ext[num])
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print(' ')
        if resp == 'N':
            print('Finalizando o programa...')
            break