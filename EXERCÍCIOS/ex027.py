### PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA ###

nome = str(input('Digite seu nome: ')).strip()

d = nome.split()

print(f'\nPrimeiro nome: {d[0]}')
print(f'Último nome: {d[-1]}\n')