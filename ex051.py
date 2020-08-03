'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.'''

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = pt + 10*r
for i in range (pt,dec,r):
    print(i,end=' ')