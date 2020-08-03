#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = int(input('Informe o ângulo que deseja: '))
print(f'O ângulo de {ang} tem o seno de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cos(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem a tangente de {tan(radians(ang)):.2f}')
