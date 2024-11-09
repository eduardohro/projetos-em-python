### TUPLAS COM TIMES DE FUTEBOL ###

brasileirao = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Internacional',
                'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 
                'Vasco da Gama', 'Atlético-MG', 'Grêmio', 'EC Vitória', 
                'Corinthians', 'Fluminense', 'Criciúma', 
                'Bragantino', 'Atlético-PR', 'Juventude', 'Cuiabá', 
                'Atlético-GO')
separação = '=-'*30

print(separação)
print(f'Listas de times do Brasileirão: {brasileirao}')
print(separação)

print(f'Os 5 primeiros são: {brasileirao[0:5]}')
print(separação)

print(f'Os 4 Últimos são: {brasileirao[-4:]}')
print(separação)

print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(separação)

# 1ª forma de se fazer 
time = 'Flamengo'
indice = brasileirao.index(time) + 1
print(f'O Flamengo está na {indice}ª posição')
print(separação)

# 2 ª forma de se fazer
print(f'O Flamengo está na {brasileirao.index("Flamengo")+1}ª posição')
print(separação)