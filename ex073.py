'''Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time Santos.'''

times = ('Atlético-MG','Vasco da Gama','Internacional','Bahia','Athletico-PR','Grêmio','Atlético-GO','Santos',
         'Fluminense','Sport Recife','São Paulo','Flamengo','Palmeiras','Botafogo','Bragantino-SP','Corinthians',
         'Goiás','Ceará SC', 'Fortaleza','Coritiba')

print(f'Lista de times do Brasileirão: {times}')
print(' ')
print('Os 5 primeiros colocados são: ',end='')
for time in times[0:5]:
    print(time,end=' ')
print(' ')
print('\nOs 4 últimos são: ',end='')
for time in times[-4:]:
    print(time,end=' ')
print(' ')
print(f'\nTimes em ordem alfabética: {sorted(times)}')
print(' ')
print(f'O Santos está na {times.index("Santos")+1}ª posição da tabela.')