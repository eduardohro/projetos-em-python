### ANALISADOR DE TEXTOS ###
nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')

se = nome.replace(' ', '')
n = nome.split()

print(f'Seu nome tem no total {len(se)} letras!')
print(f'Seu primeiro nome é {n[0]} e ele tem {len(n[0])} letras!')