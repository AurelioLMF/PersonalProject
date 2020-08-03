#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite uma medida em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida *10
cm = medida * 100
mm = medida * 1000

print(f'''A medida de {medida}m corresponde a:
{km} km
{hm} hm
{dam} dam
{dm:.0f} dm
{cm:.0f} cm
{mm:.0f} mm''')

