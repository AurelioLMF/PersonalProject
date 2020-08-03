#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input('Informe a cidade que você nasceu: ')).upper().strip()
print(cid[:5] == 'SANTO')
