### TABUADA V.2.0 ###

print('=-=' * 8)
print('\tTABUADA')
print('=-=' * 8)

num = int(input('Digite um número para saber sua tabuada: '))
print(f'Tabuada de {num}:')

for c in range(1, 11):
    print(f'{num} x {c} = \033[32m{num * c}\033[m')